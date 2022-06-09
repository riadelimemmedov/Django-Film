from django.urls import path
from .views import *

app_name = 'actor'

urlpatterns = [
    path('actorlist',actorListView,name='actorListView'),
    path('<slug>',actorDetailView,name='actorDetailView'),
]

