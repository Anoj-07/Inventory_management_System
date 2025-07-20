from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField()
    type = models.ForeignKey(ProductType)  # OTM
    departments = models.ManyToManyField(Department) #MTM

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

class Purchase(models.Model):
    product = models.ForeignKey(Product) # OTM
    price = models.FloatField()
    vendor = models.ForeignKey(Vendor) # OTM
    quantity = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

class Sell(models.Model):
    product = models.ForeignKey(Product) #OTM
    price = models.FloatField()
    customer = models.ForeignKey(Customer) #OTM
    quantity = models.IntegerField() 