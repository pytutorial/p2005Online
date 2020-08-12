from django.shortcuts import render
from .forms import *

def index(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html',
                 {'categoryList' : categoryList})

def createCategory(request):
    return render(request, 'category/form.html')    
