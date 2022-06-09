import json
from math import radians
from posixpath import sep
from pprint import pprint
from django.shortcuts import redirect, render,get_object_or_404
from django.core import serializers
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
import requests
from ratingmovie.models import *
from profiles.models import *
from .models import *
# Create your views here.

#@xframe_options_exempt => Bura helelik bele qalsin duzelende yeniden islederem
#@xframe_options_exempt
#!HomeView
def homeView(request):
    movies = Movie.objects.all()
    topfive_actors_stars = Actor.objects.all().order_by('-actor_imbd').filter(duty_type_actor='Actorisa')[:5]
    slider_movies = Movie.objects.all().filter(slider_movie=True)
    theater_movies = Movie.objects.all().filter(theater_movie=True)
    ontv_movies = Movie.objects.all().filter(ontv_movie=True)
    
    top_five_stars_duty_type = []
    top_five_stars_imdb = []
    
    for i in range(0,len(topfive_actors_stars)):
        top_five_stars_duty_type.append(topfive_actors_stars[i].duty_type_actor)
        top_five_stars_imdb.append(topfive_actors_stars[i].actor_imbd)
        #print('Duty Type : {} IMB : {}'.format(top_five_stars_duty_type,top_five_stars_imdb))
    
    context = {
        'movies': movies,
        'topfive_actors_stars': topfive_actors_stars,
        'top_five_stars_duty_type':top_five_stars_duty_type,
        'top_five_stars_imdb':top_five_stars_imdb,
        'slider_movies': slider_movies,
        'theater_movies': theater_movies,
        'ontv_movies': ontv_movies,
    }
    return render(request,'movie/home.html',context)

#@xframe_options_exempt
#!DetailView
returnajaxvalue = None
def detailView(request,slug):
    movie = get_object_or_404(Movie,slug_movie=slug)
    movies = Movie.objects.all()
    profileratemiviejs = Profile.objects.get(user=request.user)
    ratemovie_id = None
    
    #?rate movie
    ratemoviejs = RatingMovie.objects.filter(profile=profileratemiviejs,movie=movie)
    print('Rate Olunan Film ')
    for i in ratemoviejs:
        if(i.id):
            ratemovie_id = i.id
    
    print(request.user)

    #scope add
    favoriteFilmsList = None
    if(request.user.is_authenticated):
        profileUser= Profile.objects.get(user=request.user)
        print('Profile User',profileUser)
        #?fuck burdada xeta var
        
        favoriteFilmProfile = None
        if(FavoriteFilms.objects.filter(profile=profileUser).exists()):
            favoriteFilmProfile = FavoriteFilms.objects.get(profile=profileUser)
            print('User var idi onsuz')
        else:
            favoriteFilmProfile = FavoriteFilms(profile=profileUser,id=21)
            print('USER FAVORIT indi yarandi')
            
        #favoriteFilmProfile = FavoriteFilms.objects.get(profile=profileUser)
        favoriteFilmsList = favoriteFilmProfile.films.all() 
        for i in favoriteFilmsList:
            if(i.title_movie == movie.title_movie):
                print('bu film var')
                favoriteFilmsList = i.slug_movie
                break
            else:
                print('Bu film yoxdur favarit siyahida')
                favoriteFilmsList = 'yox'
        #favoriteFilmProfile.films.all()
    else:
        print('Giris Yap')
    isFavorite = None
    
    
    allmoviecategoryies = []
    relatedcategorymovie = []
    
    for i in movies:
        allmoviecategoryies += i.category_movie.all()
    
    oddmoviecategorys = []
    for k in movie.category_movie.all():
        oddmoviecategorys.append(k)

    for category in list(dict.fromkeys(allmoviecategoryies)):
        if category in oddmoviecategorys:
            relatedmovie = Movie.objects.filter(Q(category_movie=category)).distinct()
            relatedcategorymovie += relatedmovie
    filmler = []
    def moviecategory():
        for mc in list(dict.fromkeys(relatedcategorymovie)):
            if str(movie.title_movie) != str(mc):
                if(str(mc) == None):
                    pass
                else:
                    mc.date_created_movie = mc.date_created_movie.strip().split(',')[1]
                    filmler.append(mc)
        

    #!Post request Ajax
    if request.method == 'POST':
        targetvalueselect = request.POST.get('targetvalueselect')
        if targetvalueselect == 'ratingdesc':
            ratingdesc = serializers.serialize('json',set(relatedcategorymovie))
            returnajaxvalue = ratingdesc
            dolumurating_desc = False
            if(ratingdesc):
                dolumurating_desc = True
            else:
                dolumurating_desc = False
            return JsonResponse({'ratingdesc':ratingdesc,'dolumurating_desc':dolumurating_desc},safe=False)
        elif targetvalueselect == 'ratingasc':
            #ratingasc = list(relatedmovie.exclude(slug_movie=slug).order_by('avarage_ibdm').values())
            ratingasc = serializers.serialize('json',set(relatedcategorymovie))
            returnajaxvalue = ratingasc
            dolumurating_asc=False
            if(ratingasc):
                dolumurating_asc = True
            elif(ratingasc==''):
                dolumurating_asc = False
            return JsonResponse({'ratingasc':ratingasc,'dolumurating_asc':dolumurating_asc},safe=False)
        elif targetvalueselect == 'datedsc' or targetvalueselect == 'dateasc':
            datedesc = serializers.serialize('json',set(relatedcategorymovie))
            dolumudate_desc = False
            if(datedesc):   
                dolumudate_desc = True
            elif(datedesc == ''):
                dolumudate_desc = False
            return JsonResponse({'datedesc':datedesc,'dolumudate_desc':dolumudate_desc,'targetvalueselect':targetvalueselect},safe=False)
        
    moviecategory()
    return render(request,'movie/detailfilm.html',{'movie':movie,'filmler':filmler,'favoriteFilmsList':favoriteFilmsList,'ratemovie_id':ratemovie_id})


#!popularFilmView
def popularFilmView(request):
    return render(request,'movie/trendingmovieapi.html')


#!movieDetailForApi
def movieDetailForApi(request,id):
    
    #*MovieData From Api
    responsemovie = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=6eb08bbd168a23902ff08b4d31a3c687&language=en-US")
    returndatapifilm =  responsemovie.json()
    
    movieimage = returndatapifilm['backdrop_path']
    moviebudget = returndatapifilm['budget']
    moviecategory = returndatapifilm['genres']
    homepage = returndatapifilm['homepage']
    movielanguage = returndatapifilm['original_language']
    movietitle = returndatapifilm['original_title']
    moviedescription = returndatapifilm['overview']
    moviecreatedcountry = returndatapifilm['production_countries'][0]['name']
    moviecreatedate = returndatapifilm['release_date']
    moviemoney = returndatapifilm['revenue']
    movieruntime = returndatapifilm['runtime']    
    movietag = returndatapifilm['tagline']
    movieimdb = returndatapifilm['vote_average']
    moviecountvote = returndatapifilm['vote_count']
    
    #change format movieimage
    movieimage = f"https://image.tmdb.org/t/p/w500/{movieimage}"
    ###################################################################################################################################################################################
    
    
    
    
    #*MovieActor From Api 
    responseactor = requests.get(f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=6eb08bbd168a23902ff08b4d31a3c687&language=en-US")
    returndatapiactor = responseactor.json()
    
    
    
    director_list = []
    writer_list = []
    producer_list = []
    for i in returndatapiactor['crew']:
        if(i['job']=='Director'):
            director_list.append((i['original_name'],i['id']))
        elif(i['job']=='Writer'):
            writer_list.append((i['original_name'],i['id']))
        elif(i['job']=='Producer'):
            producer_list.append((i['original_name'],i['id'])) 
    
    
    #*SimilarMovieApi
    responsesimilarmovie = requests.get(f"https://api.themoviedb.org/3/movie/634649/similar?api_key=6eb08bbd168a23902ff08b4d31a3c687&language=en-US&page=1")
    returnapisimilarmovie =  responsesimilarmovie.json()
    
    similarmovieslist = []
    similarcastlist = []
    sayac = 0
    for j in returnapisimilarmovie['results']:    
        similarmovieslist.append(j)
    
    context = {
        #FilmData
        'movieimage':movieimage,
        'moviebudget':moviebudget,
        'moviecategory':moviecategory,
        'homepage':homepage,
        'movielanguage':movielanguage,
        'movietitle':movietitle,
        'moviedescription':moviedescription,
        'moviecreatedcountry':moviecreatedcountry,
        'moviecreatedate':moviecreatedate,
        'moviemoney':moviemoney,
        'movieruntime':movieruntime,
        'movietag':movietag,
        'movieimdb':movieimdb,
        'moviecountvote':moviecountvote,
        
        #Cast and Crew
        'director_list':director_list,
        'writer_list':writer_list,
        'producer_list':producer_list,
        'idvalue':id,
        'cast_list': returndatapiactor['cast'][0:10],
        'cast_list_top_five':returndatapiactor['cast'][0:5],
        
        #SimilarMovie
        'similarmovieslist':similarmovieslist,
        'similarmovieslistlenght':len(similarmovieslist),
    }
    return render(request,'movie/detailApiFilm.html',context)


def castcrewDetailForApi(request,id):
    responseCastCrewSingleData = requests.get(f"https://api.themoviedb.org/3/person/{id}?api_key=6eb08bbd168a23902ff08b4d31a3c687&language=en-US").json()
    castcrewStarredMovie = requests.get(f"https://api.themoviedb.org/3/person/{id}/movie_credits?api_key=6eb08bbd168a23902ff08b4d31a3c687&language=en-US").json()['cast'][:3]

    context = {
        'singleDataActor':responseCastCrewSingleData,
        'castcrewStarredMovie':castcrewStarredMovie
    }
    
    return render(request,'movie/detailCastCrew.html',context)


def allMoviesListView(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies,4)
    page = request.GET.get('page')
    paged_movie = paginator.get_page(page)
    
    if request.method == 'POST':
        if request.POST.get('datareconginizeid'):
            paged_movie = paginator.get_page(page)
            inputSearchText = request.POST.get('inputSearchText')
            a = request.POST.get('urlvalue')
            homeUrl = a.replace(f"movies/?page={page}",'')
            
            if(inputSearchText):
                findMovies = Movie.objects.filter(Q(title_movie__icontains=inputSearchText))
                print(len(findMovies))
                serilazersFindMovie = serializers.serialize('json',findMovies)
                return JsonResponse({'serilazersFindMovie':serilazersFindMovie,'findCountMovie':len(findMovies),'page':page,'homeUrl':homeUrl},safe=False)
    context = {
        'movies':paged_movie,
        'allmovie':movies,
        
        'paginator':paginator,
    }
    return render(request,'movie/movielist.html',context)


def addToFavoriteListFilm(request):
    
    if request.method == 'POST':
        slugurlfield = request.POST.get('slugurlfield')
        isActive = request.POST.get('isActive')
        addedFilm = Movie.objects.get(slug_movie=slugurlfield)
        currentProfile = Profile.objects.get(user=request.user)
    
        if(FavoriteFilms.objects.filter(profile=currentProfile).exists()):
            favorite_added_film = FavoriteFilms.objects.get(profile=currentProfile)
            favorite_added_film.films.add(addedFilm)
            favorite_added_film.save()
            print('Evvelceden var idi listem')
        else:
            favorite_added_film = FavoriteFilms(profile=currentProfile)
            favorite_added_film.save()
            favorite_added_film.films.add(addedFilm)
        
        if(isActive == 'false'):
            if(FavoriteFilms.objects.filter(profile=currentProfile).exists()):
                favorite_added_film = FavoriteFilms.objects.get(profile=currentProfile)
                favorite_added_film.films.add(addedFilm)
                favorite_added_film.save()
                return JsonResponse({'isAdd':'false'})
            else:
                favorite_added_film = FavoriteFilms(profile=currentProfile)
                favorite_added_film.save()
                favorite_added_film.films.add(addedFilm)
                return JsonResponse({'isAdd':'false'})
            
        elif(isActive == 'true'):
            if(FavoriteFilms.objects.filter(profile=currentProfile).exists()):
                favorite_added_film = FavoriteFilms.objects.get(profile=currentProfile)
                favorite_added_film.films.remove(addedFilm)
                favorite_added_film.save()
                print('Film Silindi')
                return JsonResponse({'isAdd':'true'})
            else:
                print('Xeta var')
            
        else:
            print('Xeta')
        
        return JsonResponse({'workResponse':'Successfully Response Favorite Film List'})


def rateFilmView(request):
    if request.method == 'POST':
        id_film = request.POST.get('id_film')
        rate_num = request.POST.get('rate_num')
        ratedfilmid = request.POST.get('rated_film_id')
        
        profile_rate = Profile.objects.get(user=request.user)
        movie_rate = Movie.objects.get(id=id_film)

        try:
            resultmovie = RatingMovie.objects.get(movie=movie_rate,profile=profile_rate)
            resultmovie.score = rate_num
            resultmovie.save()
            return JsonResponse({'score':rate_num})
        except RatingMovie.DoesNotExist:
            rating_movie_model = RatingMovie(profile=profile_rate,movie=movie_rate,score=rate_num)
            rating_movie_model.save()
            return JsonResponse({'ugurlu':'true','score':rate_num,'rated_film_id':rating_movie_model.id},safe=False)
    #else
    return JsonResponse({'xeta':'false'},safe=False)
