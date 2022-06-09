from django.shortcuts import redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from movie.models import *
import re
from .forms import *
from .models import *


#!profilePicViewContext function
def profilePicViewContext(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic_user_navbar = profile_obj.avatar
        return {'pic_user_navbar':pic_user_navbar}
    #else well => return{} = else yeni 
    return{}

#!loginView
@csrf_exempt
def loginView(request):
    if request.method == 'POST':        
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('checkrememberme')
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if remember == 'true':
                request.session.set_expiry(24*3)
                request.session.modified = True
            return JsonResponse({'success': 'Succeseed Login'})
        else:
            return JsonResponse({'error':'Error Login'})
        
    return{'error':'error login'} 

#!registerView
@csrf_exempt
def registerView(request):
    if request.method == 'POST':
        usernameRegister = request.POST.get('usernameRegister')
        emailRegister = request.POST.get('emailRegister')
        passwordRegister = request.POST.get('passwordRegister')
        repasswordRegister = request.POST.get('repasswordRegister')
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex,emailRegister) and passwordRegister==repasswordRegister:
            if(User.objects.filter(username=usernameRegister).exists()):
                return JsonResponse({'error_register':'Username already exists'})
            else:
                if(User.objects.filter(email=emailRegister).exists()):
                    return JsonResponse({'error_register':'Email already exists'})
                else:
                    user = User.objects.create_user(username=usernameRegister,email=emailRegister,password=repasswordRegister)
                    login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                    return JsonResponse({'success_register':'register successfully'})
        else:
            print('Error email format')
            return JsonResponse({'error_register':'Please enter valid email format'})
    return{'error':'error register'}

@csrf_exempt
def searchFilmView(request):
    if request.method == 'POST':
        res = None
        filmName = request.POST.get('filmName')
        films = Movie.objects.filter(title_movie__icontains=filmName).distinct()
        if len(films) > 0 and len(filmName) > 0:
            data = []
            for film in films:
                item = {
                    'pk':film.pk,
                    'title':film.title_movie,
                    'imagemovie':str(film.image_movie.url),
                    'slugmovie':film.slug_movie
                }
                data.append(item)
            res = data
        else:
            res = 'No found films...'
        return JsonResponse({'data':res})
    return{'error':'error search enter'}

