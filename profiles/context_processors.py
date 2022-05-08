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

#!loginView function
# def loginView(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST or None)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             remember_me = form.cleaned_data.get('remember_me')

#             user = authenticate(request,username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 if remember_me:#eger falsedursa
#                     request.session.set_expiry(24*3)
#                     request.session.modified = True
#                 return redirect('postblog:postListView')
#             else:
#                 form.add_error(None,'Not Found User')
#                 return{'form':form}
#         else:
#             print('Loginde Xeta')
#             return redirect('movie:home')
#     return{'loginform':form}

#!loginView
@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        print('post requesst atildi login url e giris etmek ucun')
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('checkrememberme')#burdan gelen check deyerine gore session qoyub ve ya qoymamagi sececiyik
        
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
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')#yeni biz bura deyer verende onu regex kimi scan edir,amma normal bir deyeri geri donderir verilen list ve ya objectde tapilan deyeri yeni
        if re.fullmatch(regex,emailRegister) and passwordRegister==repasswordRegister:
            if(User.objects.filter(username=usernameRegister).exists()):
                print('This username already exists')
                return JsonResponse({'error_register':'Username already exists'})
            else:
                if(User.objects.filter(email=emailRegister).exists()):
                    print('Thie email already exists')
                    return JsonResponse({'error_register':'Email already exists'})
                else:
                    user = User.objects.create_user(username=usernameRegister,email=emailRegister,password=repasswordRegister)
                    print('Created user successfully')
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
        print(filmName)
        films = Movie.objects.filter(title_movie__icontains=filmName).distinct()
        print(films)
        if len(films) > 0 and len(filmName) > 0:
            data = []
            for film in films:
                item = {
                    'pk':film.pk,
                    'title':film.title_movie,
                    'imagemovie':str(film.image_movie.url),
                    'slugmovie':film.slug_movie
                }#her loop dan yarat bir object her bir filme gore,yeni her tiklanada request atilacag bura ve hemin girilen deyerin olub olmamagi yoxlanacag databasede
                data.append(item)#json formatina cevirdi bu formada bir list yaradib icine object olanda json formati olur
            res = data
        else:
            res = 'No found films...'
        return JsonResponse({'data':res})
    return{'error':'error search enter'}

