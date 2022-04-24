from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render,reverse,HttpResponse
from django.urls import reverse_lazy
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import UpdateView,DeleteView
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


#!CommentUpdateView
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    context_object_name = 'updatecomment'
    template_name = 'postblog/update_comment.html'
    
    def get_success_url(self,**kwargs):
        postfilm = Comment.objects.get(pk=self.object.pk)
        print(postfilm.post_film.pk)
        return reverse_lazy('postblog:postDetailView',args=(postfilm.post_film.pk,))

#!DeleteCommentView
class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'postblog/delete_comment.html'
    
    def get_object(self,*args,**kwargs):
        comment_obj = super(DeleteCommentView,self).get_object(*args,**kwargs)
        if not comment_obj.user.user == self.request.user:
            raise ValueError('You have to be the owner of this comment to delete it')
        return comment_obj
    
    def get_success_url(self,*args,**kwargs):
        postfilm = Comment.objects.get(pk=self.object.pk)#self.object.pk yeni secili olan deletede olan objectin pk deyeri yeni id deyerini getir => self.object.pk seklinde
        return reverse_lazy('postblog:postDetailView',args=(postfilm.post_film.pk,))

#!categoryListPostFilmView
def categoryListPostFilmView(request,slug):
    postImageListsCategory = []
    categorys_blog = PostFilm.objects.filter(category_post__slug_category__icontains=slug)
    for pl in categorys_blog:
        postImages = ImagePost.objects.filter(postfilm_fk=pl)
        postImageListsCategory.append(postImages[0])
    context = {
        'slug':slug,
        'categorys_blog':categorys_blog,
        'postImageListsCategory':postImageListsCategory
    }
    return render(request,'postblog/category_post.html',context)

#!postFilmUpdateView
def postFilmUpdateView(request,id):
    post_film = PostFilm.objects.get(id=id)#sag terefdeki id deyeri url den gelen id deyeridir
    form = UpdatePostFilm(request.POST or None,request.FILES or None,instance=post_film)
    
    if request.method == 'POST':
        if form.is_valid():
            postfilm = form.save(commit=False)
            postfilm.author_post.user = request.user
            postfilm.save()
            return redirect('postblog:postListView')
    
    return render(request,'postblog/update_post_film.html',{'form':form})

def postFilmDeleteView(request,id):
    post_film = get_object_or_404(PostFilm,id=id)
    post_film.delete()
    return redirect('postblog:postListView')
