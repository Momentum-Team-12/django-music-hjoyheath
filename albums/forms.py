from django import forms
from .models import Album



class Album(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'title',
            'artist',
            'created_on',
        ]