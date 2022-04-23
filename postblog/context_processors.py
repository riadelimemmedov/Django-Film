from .models import *

def blogFilm(request):
    category = Category.objects.all()
    blogfilms = PostFilm.objects.all()
    popularBlogFilms = PostFilm.objects.order_by('-created_date_post')[:3]
    popularTagFilms = Tag.objects.all().order_by()[:10]
        
    tagFilms = None
    if(len(popularTagFilms) <= 7):
        tagFilms = popularTagFilms
    else:
        tagFilms = popularTagFilms

    return{
        'category': category,
        'popularBlogFilms':popularBlogFilms,
        'tagFilms':tagFilms
    }