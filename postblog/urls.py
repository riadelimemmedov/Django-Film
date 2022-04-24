from django.urls import path
from .views import *

app_name = 'postblog'

urlpatterns = [
    path('blogdetail/<int:id>/',postDetailView,name='postDetailView'),
    path('blogcreate/',postCreateView,name='postCreateView'),
    path('bloglist/',postListView,name='postListView'),
    path('like-unlike-comment/',likeunlikeCommentView,name='likeUnlikeCommentView'),
    path('update-comment/<pk>/',CommentUpdateView.as_view(),name='commentUpdateView'),
    path('delete-comment/<pk>/',DeleteCommentView.as_view(),name='commentDeleteView'),
    path('category/<slug:slug>/',categoryListPostFilmView,name='categoryListPostFilmView'),
    path('update-post-film/<int:id>/',postFilmUpdateView,name='postFilmUpdateView'),
    path('delete-post-film/<int:id>/',postFilmDeleteView,name='postFilmDeleteView')
]