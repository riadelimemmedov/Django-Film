from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(FilmCategoryMovie)
admin.site.register(TagMovie)
admin.site.register(ActorTag)
admin.site.register(Actor)
admin.site.register(Movie)