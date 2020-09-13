from django.db import models
class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True, 
                upload_to='static/images')
    def __str__(self):
        return self.name
