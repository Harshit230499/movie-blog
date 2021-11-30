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
    path('contact', views.contact , name = 'contact')

]
