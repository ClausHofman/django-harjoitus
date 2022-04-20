from django.urls import path #1
from . import views #1


urlpatterns = [
    path('', views.home), #1 find url path and trigger function in views.py
    path('products/', views.products), #1
    path('customer/', views.customer), #1
]