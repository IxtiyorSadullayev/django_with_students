from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name=models.CharField(max_length=50)
    about=models.TextField()
    price=models.IntegerField()
    photo=models.ImageField(upload_to='product')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_created=True)