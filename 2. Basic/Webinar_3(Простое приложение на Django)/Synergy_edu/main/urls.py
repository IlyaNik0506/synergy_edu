from django.urls import path
from . import views

urlpatterns = [
    path('text/', views.text),
    path('page/', views.page)
]
