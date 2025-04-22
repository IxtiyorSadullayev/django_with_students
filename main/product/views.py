from django.shortcuts import render
from .models import ProductModel
# Create your views here.


def index(request):
    products = ProductModel.objects.all()
    return render(request, 'index.html', {'products': products})