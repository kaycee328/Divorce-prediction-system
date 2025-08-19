import pytest
import pandas as pd
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from dpsproject.apps.api.models import DPS  # adjust import if needed

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="normal", password="testpass")

@pytest.fixture
def superuser(db):
    return User.objects.create_superuser(username="admin", password="adminpass")

# @pytest.fixture
def make_dps_fields(val=0):
    return {f"n{i}": val for i in range(1, 53)}

@pytest.fixture
def mock_dataset(monkeypatch):
    """Monkeypatch pandas.read_csv to return fake dataset"""
    df = pd.DataFrame(
        {
            **{f"n{i}": [0, 1] for i in range(1, 53)},
            "Divorce": [0, 1],
        }
    )
    monkeypatch.setattr(pd, "read_csv", lambda *args, **kwargs: df)
    return df

@pytest.mark.django_db
def test_get_queryset_for_normal_user(client, user):
    fields = make_dps_fields(val=1)
    DPS.objects.create(user=user, divorce_status=True, **fields)
    other_user = User.objects.create_user("other", password="pass")
    DPS.objects.create(user=other_user, divorce_status=False, **fields)

    client.login(username="normal", password="testpass")
    url = reverse("dps_api")  # from DefaultRouter or manual path
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["username"] == user.username

@pytest.mark.django_db
def test_get_queryset_for_superuser(client, superuser):
    # create records for 2 users
    u1 = User.objects.create_user("u1", password="p1")
    u2 = User.objects.create_user("u2", password="p2")
    DPS.objects.create(user=u1, divorce_status=True, **{f"n{i}": 0 for i in range(1, 53)})
    DPS.objects.create(user=u2, divorce_status=False, **{f"n{i}": 0 for i in range(1, 53)})

    client.login(username="admin", password="adminpass")
    url = reverse("dps_api")
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


@pytest.mark.django_db
def test_post_creates_prediction(client, user, mock_dataset):
    client.login(username="normal", password="testpass")
    url = reverse("dps_api")

    payload = {f"n{i}": 1 for i in range(1, 53)}

    response = client.post(url, payload, format="json")

    assert response.status_code == 201
    obj = DPS.objects.get(user=user)
    assert obj.divorce_status in [True, False]  # comes from model prediction


# @pytest.mark.django_db
# def test_post_updates_existing_instance(client, user, mock_dataset):
#     client.login(username="normal", password="testpass")
#     url = reverse("dps_api")

#     # Create an initial DPS record
#     dps = DPS.objects.create(user=user, n1=0, n2=0, divorce_status=False)

#     payload = {f"n{i}": 1 for i in range(1, 53)}

#     response = client.post(url, payload, format="json")

#     assert response.status_code == 200 or response.status_code == 201
#     dps.refresh_from_db()
#     assert dps.divorce_status in [True, False]
