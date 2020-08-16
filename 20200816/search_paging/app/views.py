from django.shortcuts import render

# Create your views here.
from .models import *

def getPriceRangeValue(priceRange):
    if priceRange == 1: return (0, 5)
    if priceRange == 2: return (5, 10)
    if priceRange == 3: return (10, 20)
    if priceRange == 4: return (20, None)
    return (None, None)

def index(request):
    categoryId = request.GET.get('categoryId', '')
    categoryId = int(categoryId) if categoryId else ''

    priceRange = request.GET.get('priceRange', '')
    priceRange = int(priceRange) if priceRange else ''
    minPrice, maxPrice = getPriceRangeValue(priceRange)

    keyword = request.GET.get('keyword', '')
    productList = Product.objects.filter(name__contains=keyword)
    
    if minPrice: 
        productList = productList.filter(price__gte=minPrice) 

    if maxPrice:
        productList = productList.filter(price__lte=maxPrice)

    productList = productList.filter(category__id=categoryId)
    categoryList = Category.objects.all()
    context = {
        'priceRange': priceRange,
        'categoryId': categoryId,
        'keyword': keyword,
        'categoryList': categoryList,
        'productList':  productList
    }
    return render(request, 'index.html' , context)
