from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('myprofile/',myProfileView,name='myProfileView')
]