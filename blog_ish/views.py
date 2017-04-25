from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post, User


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
    user = get_object_or_404(User, pk=user_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog_ish/post.html', {'post': post})
    
def userPage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'blog_ish/userPage.html', {'user': user})
    
def new_Post(request, user_id):
    return HttpResponse("New post will be made by %s" %user_id)


# Create your views here.
