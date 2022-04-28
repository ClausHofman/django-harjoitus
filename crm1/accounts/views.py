from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):
    # query orders and customers
    orders = Order.objects.all()
    customers = Customer.objects.all()

    # create dictionary
    context = {'orders':orders, 'customers':customers}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all() # query database

    return render(request, 'accounts/products.html', {'products':products}) # pass products into template with dictionary

def customer(request):
    return render(request, 'accounts/customer.html')