from django.shortcuts import render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.http import JsonResponse
from django.db.models import Q
from movie.models import *
# Create your views here.

#!actorListView
def actorListView(request):
    actors = Actor.objects.all()
    actors_top_five_related_time = Actor.objects.filter(duty_type_actor='Actorisa').order_by('-id')[:5]
    paginator = Paginator(actors,8)
    page = request.GET.get('page')
    pages_actors = paginator.get_page(page)#gedilen seyfe yeni gedilen pagelenen seyfe de demek olar
    
    for i in actors_top_five_related_time:
        if(i.gender_actor == 'M'):
            i.duty_type_actor = 'Actor'
        elif(i.gender_actor == 'F'):
            i.duty_type_actor = 'Actress'
            
            
    if request.method == 'POST':####!burdayam   
        print('Post Request Atildi')
        first_name_actor = request.POST.get('first_name_actor')
        last_name_actor = request.POST.get('last_name_actor')
        select_gender = request.POST.get('select_gender')
    
        actor = Actor.objects.filter(gender_actor=select_gender)
        print('geldi genler',actor)
        
        
        #print(select_gender)
        
        # print('POST REQUESTDEN DATALAR GELDI DEYESEN')
        # print('#################################################################')
        
        # print('First Name',first_name_actor)
        # print('First Name',last_name_actor)
        # print('First Name',select_gender)
        # print('First Name',select_duty)
        # print('First Name',country_actor)
        
        #istifadeci secir meselen => M amma qadin adi yazir
        
        if(first_name_actor and last_name_actor and select_gender):
            find_data = Actor.objects.filter(Q(first_name_actor__iexact=first_name_actor)& #olmasa yene | eleyersen
                                            Q(last_name_actor__iexact=last_name_actor)&  #and ile baglayirsansa & isare yeni Js de && denedir yeni and ile bag;layirnsasa her iki terefdeki sert dogru olmalidir
                                            Q(gender_actor=select_gender)).distinct()
            print('tada tapildi',find_data)
            if find_data:
                actor_list = list(find_data.values())
                print(actor_list)
                print('Ajax response dondu')
                return JsonResponse({'find_actor':actor_list},safe=False)

        
        #!country ni cixardarsan butun html ve js den ajaxdan hemcinnin hemcinin viewdede temizle yerini menasizdi cunki
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

