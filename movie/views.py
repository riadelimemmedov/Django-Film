import json
from math import radians
from posixpath import sep
from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
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
    
    allmoviecategoryies = []
    relatedcategorymovie = []
    
    for i in movies:
        allmoviecategoryies += i.category_movie.all()
    
    oddmoviecategorys = []
    for k in movie.category_movie.all():
        oddmoviecategorys.append(k)

    for category in list(dict.fromkeys(allmoviecategoryies)):#fromkeys ile dublicatlari cixartdim
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
        if targetvalueselect == 'ratingdesc':#desc yeni coxdan => aza dogru
            #ratingdesc = list(relatedmovie.exclude(slug_movie=slug).order_by('-avarage_ibdm').values())
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
    return render(request,'movie/detailfilm.html',{'movie':movie,'filmler':filmler})


#!popularFilmView
def popularFilmView(request):
    return render(request,'movie/trendingmovieapi.html')


#!movieDetailForApi
def movieDetailForApi(request,id):
    print('Gelen filmiin id deyeri', id)
    return render(request,'movie/detailApiFilm.html',{'idvalue':id})