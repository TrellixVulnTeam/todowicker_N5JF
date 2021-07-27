from django.forms import ModelForm
from .models import Wicker

class WickerForm(ModelForm):
    class Meta:
        model = Wicker
        fields =['title','memo','importance']
