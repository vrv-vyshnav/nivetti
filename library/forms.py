from .models import *
from django import forms
class DetailForm(forms.ModelForm):
    class Meta:
        model = PASSIVE
        fields = "__all__"
class Clockform(forms.ModelForm):
    class Meta:
        model = CLOCK_TIMING
        fields = "__all__"
class CONNECTOR(forms.ModelForm):
    class Meta:
        model = CONNECTOR
        fields = "__all__"
class DISCRETE_ANALOG(forms.ModelForm):
    class Meta:
        model = DISCRETE_ANALOG
        fields = "__all__"
class ELECTRO_MECHANICAL(forms.ModelForm):
    class Meta:
        model = ELECTRO_MECHANICAL
        fields = "__all__"
class ANALOG_POWER(forms.ModelForm):
    class Meta:
        model = ANALOG_POWER
        fields = "__all__"
class IC_CLASS_A(forms.ModelForm):
    class Meta:
        model = IC_CLASS_A
        fields = "__all__"
class IC_MEMORY(forms.ModelForm):
    class Meta:
        model = IC_MEMORY
        fields = "__all__"
class INTERFACE_LOGIC(forms.ModelForm):
    class Meta:
        model = INTERFACE_LOGIC
        fields = "__all__"
class MECHANICAL(forms.ModelForm):
    class Meta:
        model = MECHANICAL
        fields = "__all__"
class IC_RF(forms.ModelForm):
    class Meta:
        model = IC_RF
        fields = "__all__"
class IC_SENSOR(forms.ModelForm):
    class Meta:
        model = CLOCK_TIMING
        fields = "__all__"