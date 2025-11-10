from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategoriya", related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name="Tegler", related_name='tags')
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Kateqoriya ati")
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='Teg ati')
    
    def __str__(self):
        return self.name
    


