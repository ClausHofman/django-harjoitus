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