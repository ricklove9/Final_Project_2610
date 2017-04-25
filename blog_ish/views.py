from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post


def index(request):
    latest_blog_posts = Post.objects.order_by('-date_published')[:10]
    template = loader.get_template('blog_ish/index.html')
    context = {
        'latest_blog_posts': latest_blog_posts,
    }
    return HttpResponse(template.render(context, request))
    
def new_User(request):
    response = "New User Page"
    return HttpResponse(response)

def post(request, user_id, post_id):
    response = "Username: %s Post#: %s" %(user_id, post_id)
    return HttpResponse(response)
    
def userPage(request, user_id):
    return HttpResponse("most recent postings by %s" %user_id)
    
def new_Post(request, user_id):
    return HttpResponse("New post will be made by %s" %user_id)


# Create your views here.
