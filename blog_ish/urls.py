from django.conf.urls import url
from . import views


app_name = "blog"
urlpatterns = [
    
    #/blog
    url(r'^$', views.index, name='index'),
    
    #/blog/new
    url(r'^new/$', views.new_Post, name='new_Post'),
    
    #/blog/post_number
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name='post'),
    
    #/blog/user_name/new-post
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name ='commnet'),
    
    #blog/posting
    url(r'^posting/$', views.posting, name='posting'),
    
    #blog/post_number/commenting
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name ='comment'),
    
    #blog/post_number/commenting
    url(r'^(?P<post_id>[0-9]+)/commenting/$', views.commenting, name ='commenting'),
]