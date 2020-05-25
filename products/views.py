from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    prods = Product.objects.all()
    return render(request, 'products.html',{'prods':prods})