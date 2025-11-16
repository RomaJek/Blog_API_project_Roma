from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='category', verbose_name="Kategoriya")
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Kateqoriya ati")
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='Teg ati')
    posts = models.ManyToManyField(Post, related_name='tags', verbose_name='Tagdin postlari')
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    
