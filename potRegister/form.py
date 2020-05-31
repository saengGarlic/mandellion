from django import forms
from .models import *

class potReg(forms.ModelForm):
    class Meta:
        model = Pot
        fields = ['owner', 'potName', 'location', 'potType', 'description']