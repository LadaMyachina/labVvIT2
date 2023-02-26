from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse(u'Hello, world!')

def home(request):
    return render(request, 'static_handler.html')

