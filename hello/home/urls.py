from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name = 'index'),
    path('home', views.home, name = 'home'),
    path('Home', views.home,name='home'),
    path('about', views.about, name = 'about'),
    path('blog', views.blog , name = 'blog'),
    path('blog2', views.blog2, name = 'blog2'),
    path('blog3', views.blog3, name = 'blog3'),
    path('blog4', views.blog4, name = 'blog4'),
    path('blog5', views.blog5, name = 'blog5'),
    path('blog6', views.blog6, name = 'blog6'),
    path('blog7', views.blog7, name = 'blog7'),
    path('blog8', views.blog8, name = 'blog8'),
    path('blog9', views.blog9, name = 'blog9'),
    path('contact', views.contact , name = 'contact')

]
