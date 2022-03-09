from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

#!Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User,default=1,on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    avatar = models.ImageField(upload_to='profilespicture',blank=True)
    slug_user = models.SlugField(unique=True,db_index=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args,**kwargs):
        self.slug_user = slugify(self.user.username)
        super(Profile,self).save(*args, **kwargs)
        
    def __str__(self):  
        return str(self.user)

#!Create Signal
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile,sender=settings.AUTH_USER_MODEL)#yeni yaradilan User modeli gelsin avtomatitk sekilde bura User yaradilen vaxti ve bir profile yaransin




