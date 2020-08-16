from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    keyword = request.GET.get('keyword', '')
    productList = Product.objects.filter(name__contains=keyword)
    categoryList = Category.objects.all()
    context = {
        'keyword': keyword,
        'categoryList': categoryList,
        'productList':  productList
    }
    return render(request, 'index.html' , context)
