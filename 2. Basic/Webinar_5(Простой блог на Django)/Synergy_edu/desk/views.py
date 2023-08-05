from django.shortcuts import render
from .models import Desk


def desk_home(request):
    desk = Desk.objects.all()
    return render(request, 'blog/blog.html', {'blog': desk})
# Create your views here.
