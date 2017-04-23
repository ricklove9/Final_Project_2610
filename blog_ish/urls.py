from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    
    
    url(r'new/$', views.new, name='new'),
    
    
    url(r'^(?P<user_id>[0-9a-zA-Z]+)/post/$', views.post, name='post'),
]