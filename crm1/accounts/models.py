from django.db import models
# Create your models here.
# Python classes that inherit from django models, create classes that represent database tables

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True) # null True allows to make changes to database, if we import data without a name don't get error, without it will get a default value error
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
# after creating the model, quit server and run python manage.py makemigrations

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
            ('Indoor', 'Indoor'),
            ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)   # blank don't need description
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
    )
    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL) # order will remain in database if customer is removed
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):  
        return self.product.name