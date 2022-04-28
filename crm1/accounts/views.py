from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):
    # query orders and customers
    orders = Order.objects.all()
    customers = Customer.objects.all()

    # count customers and orders
    total_customers = customers.count()
    total_orders = orders.count() # reference line 9

    delivered = orders.filter(status='Delivered').count() # filter and count orders with 'Delivered' status
    pending = orders.filter(status='Pending').count() # filter and count pending orders

    # create dictionary
    context = {'orders':orders, 'customers':customers, 
    'total_orders':total_orders, 'delivered':delivered,
    'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all() # query database

    return render(request, 'accounts/products.html', {'products':products}) # pass products into template with dictionary

def customer(request, pk_test): # add pk parameter (primary key), create dynamic view
    # query customer
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all() # query customer's child object from models field

    context = {'customer':customer, 'orders':orders}

    return render(request, 'accounts/customer.html', context)