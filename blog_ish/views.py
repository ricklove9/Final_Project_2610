from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, Comment
from django.core.urlresolvers import reverse


def index(request):
    latest_blog_posts = Post.objects.order_by('-date_published')[:10]
    template = loader.get_template('blog_ish/index.html')
    context = {
        'latest_blog_posts': latest_blog_posts,
    }
    return HttpResponse(template.render(context, request))

def new_Post(request):
    template = loader.get_template('blog_ish/newPost.html')
    context = {}
    return HttpResponse(template.render(context,request))

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog_ish/post.html', {'post': post})

def posting(request):
    post = Post.objects.create_post(request.POST.get('post', request.GET['post']))
    post.save()
    return HttpResponseRedirect(reverse('blog:index'))
    
def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog_ish/comment.html', {'post': post})

def commenting(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment.objects.create_comment(post, request.POST.get('comment', request.GET['comment']))
    comment.save()
    return HttpResponseRedirect(reverse('blog:post', args=(post.id,)))


# Create your views here.
