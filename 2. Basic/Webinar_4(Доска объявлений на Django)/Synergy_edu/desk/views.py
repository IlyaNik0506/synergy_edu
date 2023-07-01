from django.shortcuts import render
from .models import Desk


def desk_home(request):
    desk = Desk.objects.all()
    return render(request, 'desk/desk.html', {'desk': desk})
# Create your views here.
