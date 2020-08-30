#app/views_users.py
from django.shortcuts import render
from .models import *
def index(request):
    productList = Product.objects.all()
    context = {'productList' : productList}
    return render(request, 'user/index.html', context)