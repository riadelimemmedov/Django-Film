from django.urls import path
from .views import *

app_name = 'postblog'

urlpatterns = [
    path('detailbloghelelik/',postDetailView,name='postDetailView')
]