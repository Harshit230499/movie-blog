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
    #return HttpResponse("This is services page")
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('password')
        contact = Contact(email = email, password=password)
        contact.save()
        return render(request, 'thanks.html')
    return render(request, 'contact.html')
    