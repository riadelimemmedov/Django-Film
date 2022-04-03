from django.shortcuts import render
from .forms import *

# Create your views here.

#!postDetailView
def postDetailView(request):
    listimage = ['logo1.png','fancybox_sprite.png','sekilyox.png']#buunu slider gonderib yoxlamalisas duz isleyir slider ya yox
    #!note => slider tapmasam gerek gedib sadik turandakini goturum movieapp daki
    
    context = {
        'listimage': listimage
    }
    
    return render(request,'postblog/blog_detail.html',context)

def postCreateView(request):
    profile = Profile.objects.get(user=request.user)
    form = PostFilmForms(request.POST or None,request.FILES or None)
    category = Category.objects.all()
    
    if request.method == 'POST':
        if form.is_valid():
            categoryblogpost = request.POST.get('categoryblogpost')#burdaki deyeri save etmek ucun commit den istifade ederik
            x = form.save(commit=False)
            x.author_post = profile
            #x.category_post__title_category = categoryblogpost #* => xeta var burda bura baxarsan category elave etmek olmur
            x.save()
            print('Blogda Secilen Kategoriya Deyeri Geldi ', categoryblogpost)
            print('nese bir deyer geldi inputdan form')
        else:
            print('Xeta')
        
    context = {
        'form':form,
        'category':category
    }
    
    return render(request,'postblog/blog_create.html',context)