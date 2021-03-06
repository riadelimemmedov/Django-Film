from this import d
from django.db import models
from django.utils.text import slugify
from profiles.models import *

# Create your models here.
#!Category Model
class Category(models.Model):
    title_category = models.CharField(max_length=100)
    slug_category = models.SlugField(unique=True,db_index=True,blank=True)
    
    def __str__(self):
        return str(self.title_category)
    
    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.title_category)
        super(Category,self).save(*args, **kwargs)
    
    def post_count(self):
        return self.categorypost.all().count()

#!Tag Model
class Tag(models.Model):
    title_tag = models.CharField(max_length=100)
    slug_tag = models.SlugField(unique=True,db_index=True,blank=True)
    
    def __str__(self):
        return str(self.title_tag)
    
    def save(self, *args, **kwargs):
        self.slug_tag = slugify(self.title_tag)
        super(Tag,self).save(*args, **kwargs)
    
    def tag_count(self):
        return self.tagmovie.all().count()

#!Post Model
class PostFilm(models.Model):
    author_post = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='authorpost')
    title_post = models.CharField(max_length=50)
    description_post = models.TextField()
    slug_post = models.SlugField(db_index=True,blank=True)
    category_post = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categorypost',blank=True,null=True)
    tag_post = models.ManyToManyField(Tag,related_name='tagmovie',blank=True)
    update_data_post = models.DateTimeField(auto_now=True)
    created_date_post = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug_post = slugify(self.title_post)
        super(PostFilm,self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title_post)
    
    
    
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

#!LikePost Model
class LikePostFilm(models.Model):
    profile_liked = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post_liked = models.ForeignKey(PostFilm,on_delete=models.CASCADE)
    value_liked = models.CharField(max_length=50,choices=LIKE_CHOICES,default='Like')
    updated_time_like = models.DateTimeField(auto_now=True)
    created_time_like = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.post_liked)

#!ImagePost Model
class ImagePost(models.Model):
    postfilm_fk = models.ForeignKey(PostFilm,related_name='imagepostfilmfk',on_delete=models.CASCADE)
    image_post = models.ImageField(upload_to='imagepostfk',default='notfoundimages.jpg')#default='notfoundimages.jpg'  
    
    def __str__(self):
        return str(self.postfilm_fk) + ' ' + str(self.image_post)


#!Comment Model
class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post_film = models.ForeignKey(PostFilm,on_delete=models.CASCADE,related_name='commentsblogfilm')
    liked_comment = models.ManyToManyField(Profile,related_name='likedcomment',blank=True)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    
    def like_comment_count(self):
        return self.liked_comment.count()
    
    def __str__(self):
        return f"Comment Writing Post Film --- {self.post_film}"
    
    class Meta:
        ordering = ['-created']
