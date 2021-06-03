from django.urls import path
from django.conf.urls import include
from drinkmap import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('store', views.store, name='store'),
    path('user', views.user, name='user'),
]
