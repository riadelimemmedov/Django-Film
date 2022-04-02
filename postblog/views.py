from django.shortcuts import render

# Create your views here.

def postDetailView(request):
    listimage = ['logo1.png','fancybox_sprite.png','sekilyox.png']#buunu slider gonderib yoxlamalisas duz isleyir slider ya yox
    #!note => slider tapmasam gerek gedib sadik turandakini goturum movieapp daki
    
    context = {
        'listimage': listimage
    }
    
    return render(request,'postblog/blog_detail.html',context)