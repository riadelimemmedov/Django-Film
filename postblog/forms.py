from django import forms
from .models import *

class PostFilmForms(forms.ModelForm):
    title_post = forms.CharField(widget=forms.TextInput(attrs={
        'type':'text',
        'id':'title-blog',
        'value':'',
        'name':'title',
        'placeholder':'Title',
        'autofocus':'True',
    }))
    
    tag_post = forms.CharField(widget=forms.TextInput(attrs={
        'type':'text',
        'id':'tag-blog',
        'value':'',
        'name':'tags',
        'placeholder':'Tags'
    }))
    
    description_post = forms.CharField(widget=forms.Textarea(attrs={
        'id':'description-blog',
        'name':'description',
        'placeholder':'Description'
    })),
    
    image_post = forms.CharField(widget=forms.TextInput(attrs={
        'type':'file',
        'name':'images',
        'id':'blog-input-file'
    }))
    class Meta:
        model = PostFilm
        fields = ['title_post','tag_post','description_post','image_post']
    