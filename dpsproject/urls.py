from django.contrib import admin
from django.urls import path, include
from dpsproject.apps.users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from dpsproject.apps.social_auth.views import LinkedInLogin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dpsproject.apps.main.urls")),
    path("", include("dpsproject.apps.users.urls")),
    path("auth/", include("dpsproject.apps.users.handler")),
    path("api/", include("dpsproject.apps.api.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("accounts/", include("allauth.urls")),  # Required for the social login
]

urlpatterns += [
    path("linkedin/", LinkedInLogin.as_view(), name="linkedin_login"),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
