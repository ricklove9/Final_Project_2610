from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")
    
def new(request):
    response = "please go somewhere else"
    return HttpResponse(response)

def post(request, user_id):
    return HttpResponse("posting by %s." %user_id)


# Create your views here.
