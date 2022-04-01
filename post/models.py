from django.db import models
from profiles.models import *
# Create your models here.

#!Post Model
class Post(models.Model):
    author_post = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='authorpost')
    title_post = models.CharField(max_length=50)
    description_post = models.TextField()
    image_post = models.ImageField(upload_to='postimages')
    liked_post = models.ManyToManyField(Profile,default=None,blank=True,related_name='likedpost')#!burani deyisersen ayri model kimi edersen => yadda saxla burani
    update_data_post = models.DateTimeField(auto_now=True)
    created_date_post = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title_post)
