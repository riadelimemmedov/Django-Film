from .models import *

def blogFilm(request):
    category = Category.objects.all()
    blogfilms = PostFilm.objects.all()
    popularBlogFilms = PostFilm.objects.order_by('-created_date_post')[:3]
    popularTagFilms = Tag.objects.all().order_by()[:10]
    
    
    #print(popularTagFilms)
    
    
    tagFilms = None
    if(len(popularTagFilms) <= 7):
        tagFilms = popularTagFilms
        #print('Tag Film 7 den kicikdir')
    else:
        tagFilms = popularTagFilms
        #print('Tag Film 7 den boyukdur')

    
    return{
        'category': category,
        'popularBlogFilms':popularBlogFilms,
        'tagFilms':tagFilms
    }