from django import forms
from .models import *

class PostFilmForms(forms.ModelForm):
    class Meta:
        model = PostFilm
        fields = '__all__'
    