from django.shortcuts import render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from movie.models import *
# Create your views here.

#!actorListView
def actorListView(request):
    actors = Actor.objects.all()
    actors_top_five_related_time = Actor.objects.filter(duty_type_actor='Actorisa').order_by('-id')[:5]
    paginator = Paginator(actors,8)
    page = request.GET.get('page')
    pages_actors = paginator.get_page(page)
    
    for i in actors_top_five_related_time:
        if(i.gender_actor == 'M'):
            i.duty_type_actor = 'Actor'
        elif(i.gender_actor == 'F'):
            i.duty_type_actor == 'Actress'
        
        
        
        
    context = {
        'actors': actors,
        'actors_top_five_related_time':actors_top_five_related_time,
        'paginator':paginator,
        'page':page,
        'pages_actors':pages_actors,
    }
    return render(request,'actor/actorlist.html',context)

#!actorDetailView
def actorDetailView(request,slug):
    actor = Actor.objects.get(slug_actor=slug)
    movies_role_actor = Movie.objects.filter(actor_movie=actor)
            
    if(actor.duty_type_actor == 'Actorisa' and actor.gender_actor=='M'):
        actor.duty_type_actor = 'Actor'
    if(actor.duty_type_actor == 'Actorisa' and actor.gender_actor=='F'):
        actor.duty_type_actor = 'Actress'

    
    context = {
        'actor':actor,
        'movies_role_actor':movies_role_actor,
    }
    
    return render(request,'actor/actor_detail.html',context)

