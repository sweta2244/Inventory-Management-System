from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    image = models.ImageField(null = True)
    phone_number = models.IntegerField(null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class ProductType(models.Model):
    name = models.CharField(max_length=300)


class Product(models.Model):
    name = models.CharField(max_length=300)
    quantity = models.IntegerField(null=True)
    department = models.ManyToManyField('Department')
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL, null=True)
    
    
class Department(models.Model):
    name = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    
    
class Vendor(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    
    
class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL,null=True)
    
    
class Customer(models.Model):
    name = models.CharField(max_length=300)
    number = models.IntegerField()
    email = models.EmailField()