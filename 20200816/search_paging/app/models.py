from django.db import models

# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200) 
    price = models.FloatField()   