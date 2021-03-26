from django.urls import path
from django.conf.urls import url
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),   
    path('addstu',views.addstu,name="addstu"),
    path('remstu',views.remstu,name="remstu"),
    path('editstu',views.editstu,name="editstu"),
]

