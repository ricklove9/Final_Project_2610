from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def create_user(self, username, password):
        user = self.create(name_text=username)
        
        return user

class User(models.Model):
    name_text = models.CharField(max_length= 50, primary_key=True)
    date_signup = models.DateTimeField('date sign up')
    
    objects = UserManager()
    
    def __str__(self):
        return self.name_text
        

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=500)
    date_published = models.DateTimeField('date published')
    
    def __str__(self):
        return self.post_text


# Create your models here.
