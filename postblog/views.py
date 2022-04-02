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
    form = PostFilmForms(request.POST or None,request.FILES or None)
    
    context = {
        'form':form,
    }
    
    return render(request,'postblog/blog_create.html',context)