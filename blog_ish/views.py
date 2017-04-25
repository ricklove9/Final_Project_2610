from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    output = "Welcome to the main page"
    return HttpResponse(output)
    
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
