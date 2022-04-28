from django import forms
from django.forms import fields,widgets
from .models import *
from django.contrib.auth.forms import PasswordChangeForm

#!UserPasswordChange Form
class UserPasswordChange(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)#Base class inheritance
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'type':'password','placeholder':'Old Password','required':True})#required,disabled,ve s kimi htm5 de gelenm attributlar boolean tipinde olurlar yeni ya true yadaki false
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
        
        
class LoginForm(forms.Form):#forms.Form yazilanda sifirdan biz yazirig formdaki rowlari ele bil,amma forms.ModelForm yazanda databasedeki rowlara uygun html formu cixardir avtomatik olarag
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type':'text',
        'name':'username',
        'id':'username',
        'placeholder':'Input Username'
    }))
    
    #password
    #remember_me 
    #elave et
    
    