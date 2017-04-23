from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name_text = models.CharField(max_length= 50)
    date_signup = models.DateTimeField('date sign up')
    password_text = models.CharField(max_length= 15)
        

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_text = models.CharField(max_length=500)
    date_published = models.DateTimeField('date published')


# Create your models here.
