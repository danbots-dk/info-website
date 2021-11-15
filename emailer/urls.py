from django.urls import path

from . import views

urlpatterns = [
    path('sendit', views.sendit, name='sendit'),
    
]