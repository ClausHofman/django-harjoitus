from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer) #register model
admin.site.register(Product)
admin.site.register(Order)