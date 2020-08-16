from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    categoryId = request.GET.get('categoryId', '')
    categoryId = int(categoryId) if categoryId else ''
    keyword = request.GET.get('keyword', '')
    productList = Product.objects.filter(name__contains=keyword)
    productList = productList.filter(category__id=categoryId)
    categoryList = Category.objects.all()
    context = {
        'categoryId': categoryId,
        'keyword': keyword,
        'categoryList': categoryList,
        'productList':  productList
    }
    return render(request, 'index.html' , context)
