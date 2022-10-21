
from django.urls import path,include
from . import views
from apptwo import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('feedback',views.feedback,name='feedback'),
    path('passw',views.passw,name='passw'),
    path('adminlog',views.adminlog,name='adminlog'),
    path('search', views.search, name='search'),
    path('studentlog',views.studentlog,name="studentlog"),
    path('proflog',views.proflog,name="proflog"),
    path('addprof',views.addprof,name='addprof'),
    path('addstud',views.addstud,name='addstud'),
    path('profsign',views.profsign,name='profsign'),
    path('studsign',views.studsign,name='studsign'),
    path('delete',views.delete,name='delete'),
    path('delobj',views.delobj,name='delobj'),
    path('check',views.check,name="check"),
    path('changep',views.changep,name="changep"),
    path('list',views.list,name="list"),

]
