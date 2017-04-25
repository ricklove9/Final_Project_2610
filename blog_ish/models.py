from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name_text = models.CharField(max_length= 50)
    date_signup = models.DateTimeField('date sign up')
    password_text = models.CharField(max_length= 15)
    
    def __str__(self):
        return self.name_text
        

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=500)
    date_published = models.DateTimeField('date published')
    
    def __str__(self):
        return self.post_text


# Create your models here.
