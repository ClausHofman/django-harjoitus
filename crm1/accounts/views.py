from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm


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
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}

    return render(request, 'accounts/customer.html', context)

def createOrder(request):

    form = OrderForm() # form note
    if request.method == 'POST':
        # print('Printing post:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    form = Order.objects.get(id=pk)
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)