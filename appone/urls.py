from django import views
from django.urls import path
from appone import views
from appone.views import home,about,login

urlpatterns = [
    path('',views.home, name='home'),
    path('static',views.static, name='static'),
    path('about',views.about, name='about'),
    path('login',views.login, name='login'),
    path('gallary',views.gallary,name='gallary'),
    path('contact',views.contact,name='contact')
]