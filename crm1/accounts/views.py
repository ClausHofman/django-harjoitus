from django.shortcuts import render
from django.http import HttpResponse #1

# Create your views here.

def home(request): #1
    return HttpResponse('home') #1

def home(request): #1
    return HttpResponse('products') #1

def home(request): #1
    return HttpResponse('customer') #1