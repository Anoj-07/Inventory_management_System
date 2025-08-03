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
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)  # OTM
    departments = models.ManyToManyField(Department) #MTM

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase') # OTM
    price = models.FloatField()
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True) # OTM
    quantity = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sell') #OTM
    price = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True) #OTM
    quantity = models.IntegerField() 

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings') #OTM
    rating = models.IntegerField() 
    comment = models.CharField(null=True)