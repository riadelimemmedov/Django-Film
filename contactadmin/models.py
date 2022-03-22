from django.db import models
from profiles.models import *

# Create your models here.

#!ContactModel
class ContactModel(models.Model):
    contact_prof = models.ForeignKey(Profile,blank=False,on_delete=models.CASCADE)
    contact_message = models.TextField()
    
    def __str__(self):
        return str(self.contact_prof)
    
    class Meta:
        verbose_name_plural = 'Contact'