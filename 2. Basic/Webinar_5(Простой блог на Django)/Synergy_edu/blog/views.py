from django.shortcuts import render
from .models import Blog_user


def blog(request):
    blog = Blog_user.objects.all()
    return render(request, 'blog/blog.html', {'blog': blog})
