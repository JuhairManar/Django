from django import forms
from .models import BookstoreModel

class Bookstoreform(forms.ModelForm):
    class Meta:
        model=BookstoreModel
        fields=['id','book_name','author','category']