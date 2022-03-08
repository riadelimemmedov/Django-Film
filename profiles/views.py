from django.shortcuts import render
from django.http import JsonResponse
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
        
        print('usernmae', profileUsername)
        print('email',profileEmail)
        print('firstname',profileFirstName)
        print('lastname',profileLastName)
        print('country',profileCountry)
        print('state',profileState)
        
        print('################################################################')

        
        #*burda esas etmek istediyim sey gelen user dan databasede basqa biri var? exist modulu ile filan yoxlamag lazimdir sonra random filan yazmag adi deyismek ucun
        a = Profile.objects.filter(user=request.user)
        print(a)
        
        return JsonResponse({'work':True})