from .models import PASSIVE
from django import forms
class DetailForm(forms.ModelForm):
    class Meta:
        model = PASSIVE
        fields = "__all__"