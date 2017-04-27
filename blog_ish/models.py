from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class UserManager(models.Manager):
    def create_user(self, username):
        user = self.create(name_text=username)
        return user

class User(models.Model):
    name_text = models.CharField(max_length= 50, primary_key=True)
    
    objects = UserManager()
    
    def __str__(self):
        return self.name_text
        

class PostManager(models.Manager):
    def create_post(self, post_text):
        post = self.create(post_text=post_text, date_published=datetime.now())
        return post
        
class Post(models.Model):
    post_text = models.CharField(max_length=500)
    date_published = models.DateTimeField('date published')
    
    objects = PostManager()
    
    def __str__(self):
        return self.post_text
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    date_published = models.DateTimeField('date published')
    
    def __str__(self):
        return self.comment_text


# Create your models here.
