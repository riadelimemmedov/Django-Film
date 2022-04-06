from django.urls import path
from .views import *

app_name = 'postblog'

urlpatterns = [
    path('blogdetail/',postDetailView,name='postDetailView'),
    path('blogcreate/',postCreateView,name='postCreateView'),
    path('bloglist/',postListView,name='postListView'),
]