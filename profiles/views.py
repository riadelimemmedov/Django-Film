from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# Create your views here.

#!MyProfile
def myProfileView(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile':profile,
    }
    
    return render(request,'profiles/my_profile.html',context)

#!updateProfileDataView
def updateProfileDataView(request):
    if request.method == 'POST':
        print('worked method post')
        profileUsername = request.POST.get('profileUsername')
        profileEmail = request.POST.get('profileEmail')
        profileFirstName = request.POST.get('profileFirstName')
        profileLastName = request.POST.get('profileLastName')
        profileCountry = request.POST.get('profileCountry')
        profileState = request.POST.get('profileState')
        
        # print('username', profileUsername)#
        # print('email',profileEmail)#
        # print('firstname',profileFirstName)#
        # print('lastname',profileLastName)#
        # print('country',profileCountry) 
        # print('state',profileState)
        
        
        # b1 = User.objects.get(username = profileUsername)
        # print(b1.email)
        
        currentUser = User.objects.get(username=request.user.username)
        currentProfile = Profile.objects.get(user=request.user)
        
        print('Before Updated PROFILE')
        print(currentProfile.country)
        print(currentProfile.state)

        currentUser.username = profileUsername
        currentUser.email = profileEmail
        currentUser.first_name = profileFirstName
        currentUser.last_name = profileLastName
        currentUser.save()
        
        print('After Updated PROFILE')
        currentProfile.country = profileCountry
        currentProfile.state = profileState
        currentProfile.save()
        
        print(currentProfile.country)
        print(currentProfile.state)
        
        
        
        
        
        #(email=profileEmail,first_name=profileFirstName,last_name=profileLastName)
        
        print('################################################################')

        
        #*burda esas etmek istediyim sey gelen user dan databasede basqa biri var? exist modulu ile filan yoxlamag lazimdir sonra random filan yazmag adi deyismek ucun
        a = User.objects.exclude(username = request.user.username)
        print(a)
        
        
        
        #if(a.objects.filter(username=profileUsername).exists()):
        if(User.objects.exclude(username = request.user.username).filter(username=profileUsername).exists()):#!burda xeta var
            #messages.add_message(request,messages.WARNING,'This username already exists')
            return JsonResponse({'errorUsernameFind':'This username already exists'})
        else:
            return JsonResponse({'username':profileUsername})
