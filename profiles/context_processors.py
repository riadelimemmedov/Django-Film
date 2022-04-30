from django.shortcuts import redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
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

def loginView(request):
    if request.method == 'POST':
        print('post requesst atildi login url e giris etmek ucun')
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('checkrememberme')#burdan gelen check deyerine gore session qoyub ve ya qoymamagi sececiyik
        
        print('Remember Me ', remember)
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if remember == 'true':
                pass
        
        return JsonResponse({'success':'ugurlu login'},safe=False)
    return{'error':'error login'} 
