from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from movie.models import *
from django.utils.text import slugify

# Create your models here.

#!Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    avatar = models.ImageField(upload_to='profilespicture',blank=True)
    slug_user = models.SlugField(unique=True,db_index=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    isFavoriteMovie = models.BooleanField(default=False)
    
    def save(self,*args,**kwargs):
        self.slug_user = slugify(self.user.username)
        super(Profile,self).save(*args, **kwargs)
        
    def __str__(self):  
        return str(self.user)


#!FavoriteFilms

class FavoriteFilms(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    films = models.ManyToManyField(Movie,blank=True,related_name='films_list')
    
    def __str__(self):
        return (f'Favorited Profile Films List --- {self.profile}')
    
    class Meta:
        verbose_name = 'Favorite Films'
        verbose_name_plural = 'Favorite Films'

#!Create Signal
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile,sender=settings.AUTH_USER_MODEL)




