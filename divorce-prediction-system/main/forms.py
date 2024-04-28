from django.forms import ModelForm
from .models import Divorce

class DivorcePredictionForm(ModelForm):
    class Meta:
        model = Divorce # Use the model to create a form
        fields = [f'n{i}' for i in range(1, 53)] # Gets fields from n1-n52




