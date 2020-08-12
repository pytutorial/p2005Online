from django.shortcuts import render, redirect
from .forms import *

def index(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html', {'categoryList' : categoryList})

def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'category/form.html', {'form': form})    

def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'category/form.html', {'form': form})

def deleteCategory(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('/')
