from django import forms
from .models import Hit

class HitForm(forms.ModelForm):
    class Meta:
        model = Hit
        fields = ['title', 'artist']
