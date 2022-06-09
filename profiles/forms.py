from django import forms
from django.forms import fields,widgets
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import PasswordChangeForm

#!UserPasswordChange Form
class UserPasswordChange(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)#Base class inheritance
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'type':'password','placeholder':'Old Password','required':True})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'type':'password','placeholder':'New Password','required':True})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'type':'password','placeholder':'Repeat New Password','required':True})

#!ChangeImageForm
class ChangeImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['avatar'].label = False
        #self.fields['user'].queryset = Profile.objects.get(user=self.request.user)
        
        
class LoginForm(forms.Form):
    username = forms.CharField(label='',required=True,widget=forms.TextInput(attrs={
        'type':'text',
        'name':'username',
        'id':'username',
        'placeholder':'Username',
    }))
    
    password = forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={
        'type':'password',
        'name':'password',
        'id':'password',
        'placeholder':'Password',
    }))
    
    remember_me = forms.BooleanField(label='',initial=False,required=False,widget=forms.CheckboxInput(attrs={
        'type':'checkbox',
        'value':'Remember me'
    }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not(User.objects.filter(username=username)):
            self.add_error('username','Username Not Found')
            print('user not found')
        #else
        return username
        