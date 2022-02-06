from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.text import slugify

# Create your models here.

#!CategoryMovie
class FilmCategoryMovie(models.Model):
    name = models.CharField(max_length=30)
    slugcategory = models.SlugField(unique=True,db_index=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    
    def save(self,*args,**kwargs):
        self.slugcategory = slugify(self.name)
        super(FilmCategoryMovie,self).save(*args,**kwargs)
        

    
    
#!TagMovie
class TagMovie(models.Model):
    name = models.CharField(max_length=30)
    slugtag = models.SlugField(unique=True, db_index=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    
    def save(self,*args,**kwargs):
        self.slugtag = slugify(self.name)
        super(TagMovie,self).save(*args, **kwargs)
        
        
        
#!ActorTags
class ActorTag(models.Model):
    actor_tag_name = models.CharField(max_length=30)
    actor_slug_tag = models.SlugField(unique=True,db_index=True,blank=True)
    
    def __str__(self):
        return str(self.actor_tag_name)
    
    def save(self,*args,**kwargs):
        self.actor_slug_tag = slugify(self.actor_tag_name)
        super(ActorTag,self).save(*args, **kwargs)





#!Actor
class Actor(models.Model):
    
    cinsiyyet = [
        ('M','Men'),
        ('F','Woman')
    ]
    
    isci_kadro = [
        ('Director','Director'),
        ('Writer','Writer'),
        ('Actorisa','Actorisa'),
        ('Producter','Producter')
    ]
    
    first_name_actor = models.CharField(max_length=50)
    last_name_actor = models.CharField(max_length=50)
    biography_actor = models.TextField(max_length=3000)
    image_actor = models.ImageField(upload_to='actorimages',null=True,blank=True)
    date_of_birth_actor = models.CharField(max_length=50,null=True)
    gender_actor = models.CharField(max_length=50,choices=cinsiyyet)
    duty_type_actor = models.CharField(max_length=50,choices=isci_kadro)
    height_actor = models.FloatField()
    actor_imbd = models.DecimalField(max_digits=10,decimal_places=1,null=True)
    country_actor = models.CharField(max_length=30)
    slug_actor = models.SlugField(unique=True,db_index=True,blank=True)
    
    def __str__(self):
        return str(self.first_name_actor)
    
    def save(self,*args,**kwargs):
        self.slug_actor = slugify(self.first_name_actor)
        super(Actor,self).save(*args,**kwargs)

#!Movie
class Movie(models.Model):
    title_movie = models.CharField(max_length=50)
    description_movie = models.TextField(max_length=3000)
    image_movie = models.ImageField(upload_to='movieimages')
    date_created_movie = models.CharField(max_length=50,null=True)
    slug_movie = models.SlugField(unique=True,db_index=True,blank=True)
    budget_movie = models.DecimalField(max_digits=20,decimal_places=2)
    language_movie = models.CharField(max_length=30)
    actor_movie = models.ManyToManyField(Actor)
    category_movie = models.ManyToManyField(FilmCategoryMovie,related_name="category_movie")
    tag_movie = models.ManyToManyField(TagMovie)
    slider_movie = models.BooleanField(default=False)#True olanlar gorunsun sliderda yeni
    avarage_ibdm = models.FloatField(default=0)
    video_movie = models.FileField(upload_to='movieivideos',blank=False)
    video_time = models.CharField(max_length=30)
    theater_movie = models.BooleanField(default=False)
    ontv_movie = models.BooleanField(default=False)
    mmpa_rating_movie = models.CharField(max_length=30,null=True)
    
    def __str__(self):
        return str(self.title_movie)
    
    def save(self,*args,**kwargs):
        self.slug_movie = slugify(self.title_movie)
        super(Movie,self).save(*args, **kwargs)
        
    def get_category(self):
        return self.category_movie.all()
        