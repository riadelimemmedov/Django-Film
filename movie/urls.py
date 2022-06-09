from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('',homeView,name='home'),
    path('<slug:slug>',detailView,name='detailfilm'),
    path('popular/',popularFilmView,name='popularFilmView'),
    path('detailapifilm/<int:id>',movieDetailForApi,name='movieDetailForApi'),
    path('detailcastcrew/<int:id>',castcrewDetailForApi,name='castcrewDetailForApi'),
    path('movies/',allMoviesListView,name='allMoviesListView'),
    path('addtofavorite/',addToFavoriteListFilm,name='addToFavoriteListFilm'),
    path('ratefilm/',rateFilmView,name='rateFilmView')
]