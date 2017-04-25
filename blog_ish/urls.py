from django.conf.urls import url
from . import views

urlpatterns = [
    
    #/blog
    url(r'^$', views.index, name='index'),
    
    #/blog/new
    url(r'new/$', views.new_User, name='new'),
    
    #/blog/user_name
    url(r'^(?P<user_id>[0-9a-zA-Z]+)/$', views.userPage, name='userPage'),
    
    #/blog/user_name/post_number
    url(r'^(?P<user_id>[0-9a-zA-Z]+)/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    
    #/blog/user_name/new-post
    url(r'^(?P<user_id>[0-9a-zA-Z]+)/new-post/$', views.new_Post, name='new_post'),
]