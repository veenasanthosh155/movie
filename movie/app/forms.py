#Form definition

from django import forms
from app.models import Movie
class Movieform(forms.ModelForm):
    class Meta:

        model=Movie
        fields="__all__"