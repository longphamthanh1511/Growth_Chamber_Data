from django import forms
from CRUDOperation.models import Plants

class plantforms(forms.ModelForm):
    class Meta:
        model= Plants
        fields= "__all__"
