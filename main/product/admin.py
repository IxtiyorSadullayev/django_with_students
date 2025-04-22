from django.contrib import admin
from .models import ProductModel
# Register your models here.

class AdminShow(admin.ModelAdmin):
    list_display=['name', 'about', 'price', 'photo', 'created', 'updated']
    search_fields=('name', 'about', 'price')
    

admin.site.register(ProductModel, AdminShow)
