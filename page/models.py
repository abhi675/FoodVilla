from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    img=models.ImageField(upload_to='pics')

class Payment(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    email=models.EmailField()
    nameoncard=models.CharField(max_length=50)
    creditcardnumber=models.CharField(max_length=50)
    cvv=models.CharField(max_length=50)
    date=models.DateField()
    price=models.IntegerField(default=0)
    foodname=models.CharField(max_length=50)