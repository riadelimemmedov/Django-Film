from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('',homeView,name='home'),
    path('<slug:slug>',detailView,name='detailfilm'),
    path('popular/',popularFilmView,name='popularFilmView'),
    path('detailapifilm/<int:id>',movieDetailForApi,name='movieDetailForApi')
    
    #path('jsonver',jsonver,name='jsonver'),
]