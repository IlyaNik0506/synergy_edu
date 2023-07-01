from django.shortcuts import render
from django.http import  HttpResponse


def index(request):
    return HttpResponse('<h1>Hello, it’s my web-site</h1>')


def about(request):
    return HttpResponse('<h4>Страница о нас</h4>')
# Create your views here.
