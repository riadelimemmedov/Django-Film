from random import choices
from django import forms
from django.forms import fields,widgets
from .models import *

#!PostFilmForms
class PostFilmForms(forms.ModelForm):
    
    numbers = (#burda [] yazma hec baxt ic ice yaz ele bil tupleleari  amma list yazma choices de
    ('1','1 Yildiz'),
    ('2','2 Yildiz'),
    ('3','3 Yildiz'),
    ('4','4 Yildiz'),
    ('5','5 Yildiz'),
    )
    
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
    }))
    
    
    #category_post = forms.ChoiceField(widget = forms.Select(attrs={'class':'radio','class':'categoryclass'}))
    
    class Meta:
        model = PostFilm
        fields = ['title_post','tag_post','description_post','category_post']
        

#!ImagePostForm
class ImagePostForm(forms.ModelForm):
    image_post = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'type':'file',
        'name':'images',
        'id':'blog-input-file',
        'multiple':'True',
    }))
    
    class Meta:
        model = ImagePost
        fields = ['image_post']

#!CommentForm
class CommentForm(forms.ModelForm):
    body = forms.CharField(required=True,label='',label_suffix='',widget=forms.Textarea(attrs={
        'name':'message',
        'id':'',
        'placeholder':'Message',
    }))
    class Meta:
        model = Comment
        fields = ['body']

#!CommentUpdateForm
class CommentUpdateForm(forms.ModelForm):
    body = forms.CharField(required=True,label='',widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['body']
    