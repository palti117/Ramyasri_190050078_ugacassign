from django.urls import path
from django.conf.urls import url
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),   # directs to userdata.html
    path('addstu',views.addstu,name="addstu"),#interface for adding student, directs to addstu.html
    path('remstu',views.remstu,name="remstu"),#interface for removing student, directs to remstu.html
    path('editstu',views.editstu,name="editstu"),#interface for editing student details, directs to editstu.html
]

