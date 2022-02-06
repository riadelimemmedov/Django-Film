from django.urls import path
from .views import *

app_name = 'actor'

urlpatterns = [
    path('<slug>',actorDetailView,name='actorDetailView')
]