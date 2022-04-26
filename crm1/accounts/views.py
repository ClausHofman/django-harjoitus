from django.shortcuts import render
from django.http import HttpResponse #1
# Create your views here.
from .models import *


def home(request): #1
    return render(request, 'accounts/dashboard.html') #2

def products(request): #1
    return render(request, 'accounts/products.html') #2

def customer(request): #1
    return render(request, 'accounts/customer.html') #2