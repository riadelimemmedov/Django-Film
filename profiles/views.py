from django.shortcuts import render
from .models import *
# Create your views here.

#!MyProfile
def myProfileView(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile':profile,
    }
    
    return render(request,'profiles/my_profile.html',context)