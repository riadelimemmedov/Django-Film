from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
from .models import *
# Create your views here.

#!MyProfile
def myProfileView(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        if request.method == 'POST':
            form = UserPasswordChange(request.user,request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request,user)
                print('sifre degisti')
                messages.add_message(request,messages.SUCCESS,'Successfully Changed Password')
                return redirect(request.path)
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'profile':profile,
        'form':form
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
        
        #print('Before Updated PROFILE')
        #print(currentProfile.country)
        #print(currentProfile.state)

        #deyesen burda aradirmag lazimdir xetanin sebebini cunki burada save edirik burda ola biler problem
        print('################################################################')
        b = User.objects.exclude(username = request.user.username)#!last error this field

        if(User.objects.exclude(username = request.user.username).filter(username=profileUsername).exists()) or len(profileUsername)<=2:
                print('girilen isim already exists in database')
                print(len(profileUsername))
                return JsonResponse({'errorUsernameFind':'This username already exists','profileUsername':profileUsername})
            
                #break
        else:
            #print('Success Updated User Data')
            print('Bu isim databasede halen yok')
            currentUser.username = profileUsername
            currentUser.email = profileEmail
            currentUser.first_name = profileFirstName
            currentUser.last_name = profileLastName
            currentProfile.country = profileCountry
            currentProfile.state = profileState
            currentProfile.save()
            currentUser.save()
            
    
        
        #print('After Updated PROFILE')
        #print(currentProfile.country)
        #print(currentProfile.state)

        #(email=profileEmail,first_name=profileFirstName,last_name=profileLastName)
        
        #print('################################################################')

        
        #*burda esas etmek istediyim sey gelen user dan databasede basqa biri var? exist modulu ile filan yoxlamag lazimdir sonra random filan yazmag adi deyismek ucun
        a = User.objects.exclude(username = request.user.username)
        #print(a)

        
        # for i in b:
        #     #print('username other',i.username)
        #     print('################################################################')#!xeta var burdada,profile hissinseki user a unique true ver ordan filter yazag yeni Profile modelinden Userdan yaramir
        #     if(profileUsername == i.username):
        #         print('this name already exists in database')
        #         print(profileUsername)
        #     else:
        #         print('hata')
        
        
        
        # if(a.objects.filter(username=profileUsername).exists()):
        # if(User.objects.exclude(username = request.user.username).filter(username=profileUsername).exists()):#!burda xeta var
        #     #messages.add_message(request,messages.WARNING,'This username already exists')
        #     #print('fff')
        #     
        # else:
    return JsonResponse({'username':profileUsername})



def userFavoriteView(request):
    return render(request,'profiles/my_favorite.html')