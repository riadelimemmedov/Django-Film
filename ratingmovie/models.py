from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime,timedelta
from django.utils import timezone
from profiles.models import *
from movie.models import *

# Create your models here.
#!RatingMovie
class RatingMovie(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    score = models.IntegerField(default=0,validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])
    created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.score) + '-' + str(self.profile) + '-' + str(self.movie)  