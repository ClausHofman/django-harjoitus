from django.shortcuts import render
from django.http import HttpResponse #1

# Create your views here.

def home(request): #1
    return render(request, 'accounts/dashboard.html') #2

def products(request): #1
    return HttpResponse('tuotesivu') #1

def customer(request): #1
    return HttpResponse('customer') #1