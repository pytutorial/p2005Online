from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    productList = Product.objects.all()
    context = {
        'productList':  productList
    }
    return render(request, 'index.html'
                    , context)
