from .models import *

def blogFilm(request):
    category = Category.objects.all()
    blogfilms = PostFilm.objects.all()
    categoryFilmsList = []
    
    for j in category:
        # categoryfilms = i.category_post
        # say = Category.objects.filter(title_category=categoryfilms)
            categoryneyse = j.title_category
            netice = PostFilm.objects.filter(category_post__title_category=categoryneyse).distinct()
            categoryFilmsList.append(netice)
        
    return{
        'category': category
    }