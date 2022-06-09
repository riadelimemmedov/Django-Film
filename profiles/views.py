from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from ratingmovie.models import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth import login,authenticate,logout
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
        profileUsername = request.POST.get('profileUsername')
        profileEmail = request.POST.get('profileEmail')
        profileFirstName = request.POST.get('profileFirstName')
        profileLastName = request.POST.get('profileLastName')
        profileCountry = request.POST.get('profileCountry')
        profileState = request.POST.get('profileState')

        
        currentUser = User.objects.get(username=request.user.username)
        currentProfile = Profile.objects.get(user=request.user)


        if(User.objects.exclude(username = request.user.username).filter(username=profileUsername).exists()) or len(profileUsername)<=2:
                print('girilen isim already exists in database')
                print(len(profileUsername))
                return JsonResponse({'errorUsernameFind':'This username already exists','profileUsername':profileUsername})
        if(User.objects.exclude(username = request.user.username).filter(email=profileEmail).exists()):
            return JsonResponse({'errorEmailFind':'This email already exists','profileEmail':profileEmail})
        else:
            currentUser.username = profileUsername
            currentUser.email = profileEmail
            currentUser.first_name = profileFirstName
            currentUser.last_name = profileLastName
            currentProfile.country = profileCountry
            currentProfile.state = profileState
            currentProfile.save()
            currentUser.save()
    return JsonResponse({'username':profileUsername})


#!userFavoriteView
def userFavoriteView(request):
    profile = Profile.objects.get(user=request.user)
    
    filmsFavs = None
    paged_films = None
    paginator = None
    page = None
    if(FavoriteFilms.objects.filter(profile=profile).exists()):
        profFav = FavoriteFilms.objects.get(profile=profile)
        filmsFavs = profFav.films.all()
        paginator = Paginator(filmsFavs,5)
        page = request.GET.get('page')
        paged_films = paginator.get_page(page)
        currentPage = request.GET.get('currentPage')
    else:
        filmsFavs = None
    
    context = {
        'filmsFavs':paged_films,
        'profile':profile,
        'filmsAll':filmsFavs,
        'paginator':paginator,
        'page':page
    }
    
    return render(request,'profiles/my_favorite.html',context)

#!userLogoutView
def userLogoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('movie:home')
    
#!removeFavoriteFilmFromList
def removeFavoriteFilmFromList(request):
    if request.method == 'POST':

        idFilm = request.POST.get('idFilm')
        existsFilm = Movie.objects.get(id=idFilm)
        
        currentProfileUser = Profile.objects.get(user=request.user)
        favorite_removed_film = FavoriteFilms.objects.get(profile=currentProfileUser)
        allfilmslistuser = favorite_removed_film.films.all()
        favorite_removed_film.films.remove(existsFilm)
        favorite_removed_film.save()
        
        return JsonResponse({'removeFilm':'RemovedFilmData','counfFavFilm':allfilmslistuser.count()},safe=False)
    return HttpResponse('Response Remove Film List')

#!changeImageProfile

def changeImageProfile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        print('Profil Var')
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    
    if request.method == 'POST':
        form = ChangeImageForm(request.POST or None,request.FILES or None,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:myProfileView')
    else:
        form = ChangeImageForm(instance=profile)
    
    context = {
        'profile':profile,
        'form':form
    }
    return render(request,'profiles/change_image.html',context)

def rateMovieListView(request):
    profile = Profile.objects.get(user=request.user)
    profile_rated_films = RatingMovie.objects.filter(profile=profile)
    
    paginator = Paginator(profile_rated_films,3)
    page = request.GET.get('page')
    paged_rate_films = paginator.get_page(page)

    
    context = {
        'profile':profile,
        'profile_rated_films':paged_rate_films
    }
    
    return render(request,'profiles/my_rates.html',context)