from django import forms
from .models import Calculation

class Calculationform(forms.ModelForm):
    class Meta:
        model=Calculation
        fields='__all__'
        labels={
            'var1':'Number 1',
            'var2':'Number 2',
            'var3':'Result',
        }