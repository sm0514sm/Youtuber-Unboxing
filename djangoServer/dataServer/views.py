from django.shortcuts import render, HttpResponse
from .models import Video

# Create your views here.
def index(request):
    return HttpResponse('hello')

def add_video(request, videoId):
    pass

