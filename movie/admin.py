from django.contrib import admin
from .models import *
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['date_created_movie']


admin.site.register(FilmCategoryMovie)
admin.site.register(TagMovie)
admin.site.register(ActorTag)
admin.site.register(Actor)
admin.site.register(Movie,MovieAdmin)
admin.site.register(RelatedMovieModel)