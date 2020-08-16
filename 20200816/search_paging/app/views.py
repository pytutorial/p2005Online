from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    keyword = request.GET.get('keyword', '')
    productList = Product.objects.filter(name__contains=keyword)
    context = {
        'keyword': keyword,
        'productList':  productList
    }
    return render(request, 'index.html' , context)
