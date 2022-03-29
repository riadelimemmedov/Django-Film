from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('myprofile/',myProfileView,name='myProfileView'),
    path('updateprofiledata/',updateProfileDataView,name='updateProfileDataView'),
    path('myfavorite/',userFavoriteView,name='userFavoriteView'),
    path('logout/',userLogoutView,name='userLogoutView'),
    path('removefilmsfavoritelist/',removeFavoriteFilmFromList,name='removeFavoriteFilmFromList'),
    path('change-image-profile/',changeImageProfile,name='changeImageProfile'),
    path('myrates/',rateMovieListView,name='rateMovieListVie')
]
