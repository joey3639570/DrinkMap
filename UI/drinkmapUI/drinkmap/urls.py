from django.urls import path
from django.conf.urls import include
from drinkmap import views

urlpatterns = [
    path('', views.index, name='index'),
]
