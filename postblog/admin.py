from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostFilm)
admin.site.register(LikePostFilm)
admin.site.register(ImagePost)
admin.site.register(Comment)