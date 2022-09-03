from typing import ContextManager
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html' , context )

def home(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'home.html' , context )
    
def about(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'about.html' , context)

def blog2(request):
    return render(request, 'blog2.html')
   
def blog(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'blog.html', context )
def blog3(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'blog3.html', context )
def blog4(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'blog4.html', context )
def blog5(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'blog5.html', context )
def blog6(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'blog6.html', context )
def blog7(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'blog7.html', context )
def blog8(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'blog8.html', context )
def blog9(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'blog9.html', context )
    #return HttpResponse("This is services page")
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('password')
        contact = Contact(email = email, password=password)
        contact.save()
        messages.success(request,'Details sent')
        #return render(request, 'thanks.html')
    return render(request, 'contact.html')
    