from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)  # varchar(30)
    price = models.DecimalField(decimal_places=2,
                                max_digits=7)  # Decimal(7,2)
    pub = models.CharField(max_length=50,null=True)
    market_price = models.DecimalField(decimal_places=2,max_digits=7,default=0)

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    email = models.EmailField(max_length=60,null=True,blank=True)