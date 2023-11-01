from django.http import request
from django.shortcuts import render

# Create your views here.

def about():
    return render(request, 'about.html')

def contact():
    return render(request, 'contact.html')

def classes():
    return render(request, 'classes.html')
