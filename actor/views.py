from django.shortcuts import render
from movie.models import *
# Create your views here.

#!actorDetailView
def actorDetailView(request,slug):
    actor = Actor.objects.get(slug_actor=slug)
    movies_role_actor = Movie.objects.filter(actor_movie=actor)
            
    if(actor.duty_type_actor == 'Actorisa'):
        actor.duty_type_actor = 'Actor'

    
    context = {
        'actor':actor,
        'movies_role_actor':movies_role_actor,
    }
    
    return render(request,'actor/actor_detail.html',context)