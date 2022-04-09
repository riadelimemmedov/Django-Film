from multiprocessing import context
from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
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

#!postCreateView
def postCreateView(request):
    profile = Profile.objects.get(user=request.user)
    form = PostFilmForms(request.POST or None,request.FILES or None)
    imageform = ImagePostForm(request.POST or None,request.FILES or None)
    category = Category.objects.all()
    
    if request.method == 'POST':
        if form.is_valid():

                print('Requestden gelen butun deyer ', request.POST.getlist('image_post'))
                print('Requestden gelen sekil deyeri', request.FILES.getlist('images'))
                print('Requestden gelen sekil deyeri', request.FILES.getlist('image_post'))
                
                images_post = request.FILES.getlist('image_post')
                tag_post = request.POST.get('tag_post').split(',')
                
                print('Get tag value ', tag_post)
    
                tag_value = None
                x = form.save(commit=False)
                x.author_post = profile
                x.save()
                
                #!eger birden cox tag gelerse bu taglari split ile vergule gore ayiirb for loopda save etmek lazimdir bunu yazmag lazimdir
                
                for tp in tag_post:
                    if(Tag.objects.filter(title_tag=tp)):
                        if(x):
                            tag_value = Tag.objects.get(title_tag=tp)
                            x.tag_post.add(tag_value)
                        print('POST YARANDI kohne tagli')
                        # addtag = Tag.objects.get(title_tag=request.POST.get('tag_post'))
                        # x.tag_post.add(addtag) 
                    else:
                        #tag_value = request.POST.get('tag_post')
                        new_tag = Tag.objects.create(title_tag=tp)
                        new_tag.save()
                        if(x):
                            x.tag_post.add(new_tag)
                        print('yeni tagli bir post yarandi')
                    
                    
                
                # if(Tag.objects.filter(title_tag=request.POST.get('tag_post'))):
                #         if(x):
                #             tag_value = Tag.objects.get(title_tag=request.POST.get('tag_post'))
                #             x.tag_post.add(tag_value)
                #         print('POST YARANDI kohne tagli')
                #         # addtag = Tag.objects.get(title_tag=request.POST.get('tag_post'))
                #         # x.tag_post.add(addtag) 
                # else:
                #     tag_value = request.POST.get('tag_post')
                #     new_tag = Tag.objects.create(title_tag=tag_value)
                #     new_tag.save()
                #     if(x):
                #         x.tag_post.add(new_tag)
                #     print('yeni tagli bir post yarandi')
                
                if(images_post):
                    for i in images_post:
                        print('nah isleyerem')
                        imagepost = ImagePost.objects.create(
                            postfilm_fk = x,
                            image_post = i
                        )
                else:
                    imagepost = ImagePost.objects.create(postfilm_fk=x)
                
                #?Burda bug var sonra qaytararsan evvelki halina
                return redirect('postblog:postListView')
                    #imagepost.save()
                    

                # print(request.POST.get('category'))
                # categoryblogpost = request.POST.get('categoryblogpost')#burdaki deyeri save etmek ucun commit den istifade ederik
                # if x:
                #     print('Yaranan Postun Title Deyeri ', x.title_post)
                #     print('Yaranan Postun Category Deyeri ', x.category_post)
        else:
            print('Xeta')
        
    context = {
        'form':form,
        'imageform':imageform,
        'category':category
    }
    
    return render(request,'postblog/blog_create.html',context)


def postListView(request):
    postsList = PostFilm.objects.all()
    postImageLists = []
    postTitleList = []
    
    for pl in postsList:
        postImages = ImagePost.objects.filter(postfilm_fk=pl)
        #print('PostFilm for Image List ', postImages)
        print(postImages[0])
        print(postImages)
        postImageLists.append(postImages[0])
    
    postsListPagination = Paginator(postImageLists,4)
    page = request.GET.get('page')
    paged_post = postsListPagination.get_page(page)
    
    
    context = {
        'postImageLists':paged_post,
        #'firstImageList':firstImageList,
    }
    
    return render(request,'postblog/blog_list.html',context)