from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render,reverse,HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
from django.http import JsonResponse
from .forms import *

# Create your views here.

#!postDetailView
def postDetailView(request,id):
    postfilm = get_object_or_404(PostFilm,id=id)
    imagepostlists = ImagePost.objects.filter(postfilm_fk=postfilm)
    tagpostslists = postfilm.tag_post.all()
    profile = Profile.objects.get(user=request.user)

    form = CommentForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.post_film = postfilm
            instance.body = form.cleaned_data.get('body')
            form.save()
            return redirect(reverse('postblog:postDetailView',kwargs={'id':id}))#yeni postun ozune qayit ele
    context = {
        'postfilm':postfilm,
        'imagepostlists':imagepostlists,
        'tagpostslists':tagpostslists,
        'likeprofile':profile,
        'form':form,
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
    postSearchResult = []
    
    
    postsListPagination = None
    page = None
    paged_post = None
    
    for pl in postsList:
        postImages = ImagePost.objects.filter(postfilm_fk=pl)
        postImageLists.append(postImages[0])
    
    postsListPagination = Paginator(postImageLists,4)
    page = request.GET.get('page')
    paged_post = postsListPagination.get_page(page)
    
    print('Pagination Axtarisdan Evvel ', postsListPagination)
    
    
    if request.method == 'POST':
        print('Blog Axtaris Isledi')
        searchedTextBlogFilms = request.POST.get('searchedTextBlogFilms')
        if searchedTextBlogFilms:
            resultsFilms = PostFilm.objects.filter(Q(title_post__icontains=searchedTextBlogFilms)).distinct()
            postsListPagination = Paginator(resultsFilms,4)
            page = request.GET.get('page')
            paged_post = postsListPagination.get_page(page)
            for i in paged_post:
                postSearchResult.append(i)
            print('Axtarisdan Sonra Pagination ', paged_post)
            
            
    
    context = {
        'postImageLists':paged_post,
        'postSearchResult':postSearchResult
        #'firstImageList':firstImageList,
    }
    
    return render(request,'postblog/blog_list.html',context)

#bura login_required qeyt etmeyi unutma yeni yadindan cixmasin bura login required qeyd etmek
def likeunlikeCommentView(request):
    if request.method == 'POST':
        print('Like Unlike Viuew Request AtildI Ajax Ile')
        profile = Profile.objects.get(user=request.user)
        commentId = request.POST.get('commentId')
    
        comment = Comment.objects.get(id=commentId)
        
        if profile not in comment.liked_comment.all():
            comment.liked_comment.add(profile)
            return JsonResponse({'liked':'true','likecommentcount':comment.liked_comment.all().count() })
        else:
            comment.liked_comment.remove(profile)
            return JsonResponse({'liked':'false','likecommentcount':comment.liked_comment.all().count()})
        
    return HttpResponse('like unlike')