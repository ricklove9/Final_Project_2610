from django.contrib import admin
from .models import Post, User, Comment

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comment)

# Register your models here.
