from django.urls import path #1
from . import views #1

# give names to pages

urlpatterns = [
    path('', views.home, name="home"), # find url path and trigger function in views.py
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>/', views.customer,name="customer"), # use angle brackets, add <str:pk_test>/, pk_test has to be in the customer variable in view.py

    path('create_order/', views.createOrder, name="create_order")
]