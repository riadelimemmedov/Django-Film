from django import template
from movie.models import *

register = template.Library()

@register.simple_tag(name='categories')
def all_categories_movie():
    return FilmCategoryMovie.objects.all()

