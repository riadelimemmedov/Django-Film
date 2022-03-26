from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
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
    
    def __str__(self):
        return f"Rating Movie Pk Value --- {self.pk}"