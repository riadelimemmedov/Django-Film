import json
from posixpath import sep
from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.core import serializers
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
                    filmler.append(mc)
                    
    #!Post request Ajax
    if request.method == 'POST':
        targetvalueselect = request.POST.get('targetvalueselect')
        order_film_imbd = []
        if targetvalueselect == 'ratingdesc':#desc yeni coxdan => aza dogru
            ratingdesc = list(relatedmovie.exclude(slug_movie=slug).order_by('-avarage_ibdm').values())
            returnajaxvalue = ratingdesc
            print('Coxdan Aza siralandi', ratingdesc)#!Coxdan Aza siralandi <QuerySet [<Movie: La La Land>, <Movie: Guardians of the Galaxy>]>
            return JsonResponse({'ratingdesc':ratingdesc},safe=False)
        elif targetvalueselect == 'ratingasc':#eger ratingasc dirse yeni azdan => coxadir
            ratingasc = list(relatedmovie.exclude(slug_movie=slug).order_by('avarage_ibdm').values())
            returnajaxvalue = ratingasc
            print('Azdan Coxa Siralandi',returnajaxvalue)
            return JsonResponse({'ratingasc':ratingasc},safe=False)
    moviecategory()
    return render(request,'movie/detailfilm.html',{'movie':movie,'filmler':filmler})
