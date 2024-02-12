from django.db import models
from datetime import date
# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=70)
    telephone_number = models.BigIntegerField()
    telephone_number2 = models.BigIntegerField(default=0)
    

class Tickets(models.Model):
    date = models.DateField()
    ticket_number = models.BigIntegerField()
    customer_id = models.ForeignKey(Customers, on_delete=models.SET_NULL,null=True)
    product = models.CharField(max_length=30)
    trademark = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=40)
    failure = models.CharField(max_length=40)
    product_image1 = models.ImageField(upload_to="products_images/")
    product_image2 = models.ImageField(upload_to="products_images/")
    product_image3 = models.ImageField(upload_to="products_images/")
    description = models.CharField(max_length=300)
    local = models.BooleanField(default=True)

class WarrantyProducts(models.Model):
    date = models.DateField()
    ticket_id = models.ForeignKey(Tickets, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=300)
    local = models.BooleanField(default=True)

class DeliveredProducts(models.Model):
    ticket_id = models.ForeignKey(Tickets, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    invoice = models.CharField(max_length=30)
    date = models.DateField()

class CallHistory(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    description = models.CharField(max_length=300)