from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, User
from django.core.urlresolvers import reverse


def index(request):
    latest_blog_posts = Post.objects.order_by('-date_published')[:10]
    template = loader.get_template('blog_ish/index.html')
    context = {
        'latest_blog_posts': latest_blog_posts,
    }
    return HttpResponse(template.render(context, request))
    
def new_User(request):
    template = loader.get_template('blog_ish/newUser.html')
    context = {}
    return HttpResponse(template.render(context, request))

def post(request, user_id, post_id):
    user = get_object_or_404(User, pk=user_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog_ish/post.html', {'post': post, 'user': user})
    
def userPage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'blog_ish/userPage.html', {'user': user})
    
def new_Post(request, user_id):
    return HttpResponse("New post will be made by %s" %user_id)

def posting(request, user_id):
    return HttpResponse("I am posting!")
    
def CreatingUser(request, user_id):
    user = User.objects.create_user(pk.request.Post[username])
    return HttpResponse("NEW USER")

# Create your views here.
