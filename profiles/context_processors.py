from django.shortcuts import redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
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

@csrf_exempt
def registerView(request):
    if request.method == 'POST':
        usernameRegister = request.POST.get('usernameRegister')
        emailRegister = request.POST.get('emailRegister')
        passwordRegister = request.POST.get('passwordRegister')
        repasswordRegister = request.POST.get('repasswordRegister')
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')#yeni biz bura deyer verende onu regex kimi scan edir,amma normal bir deyeri geri donderir verilen list ve ya objectde tapilan deyeri yeni
        if re.fullmatch(regex,emailRegister) and passwordRegister==repasswordRegister and len(passwordRegister) >= 8:
            if(User.objects.filter(username=usernameRegister).exists()):
                print('bele bir user databasede var')
                return JsonResponse({'already_user_declared':'Username already exists'})
            else:
                if(User.objects.filter(email=emailRegister).exists()):
                    print('bele bir email artiq movcuddur')
                    return JsonResponse({'already_email_declared':'Email already exists'})
                else:
                    user = User.objects.create_user(username=usernameRegister,email=emailRegister,password=repasswordRegister)
                    print('User yaradi ugurlu bir sekilde')
                    login(request,user)
                return JsonResponse({'success_register':'register successfully'})
        else:
            print('xeta bas verdi register user zamani')
            return JsonResponse({'error_register':'register error'})
    return{'error':'error register'}