from django import forms
from django.contrib.auth.models import User #importing user for user form
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
#UserCreationForm for creating user
#UserCreationForm #importing user form
#UserChangeForm  for user data change

class Registerform(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model=User #User model as no model has defined
        fields=['username','first_name','last_name','email']
        #fields='__all__'
        
""" for field in User._meta.get_fields():
    print(field.name) """
    