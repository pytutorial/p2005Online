from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def listCategory(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html', {'categoryList' : categoryList})

@login_required
def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staff')
    return render(request, 'category/form.html', {'form': form})    

@login_required
def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/staff')
    return render(request, 'category/form.html', {'form': form})

@login_required
def deleteCategory(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('/')

#127.0.0.1:8000/list_product
@login_required
def listProduct(request):
    productList = Product.objects.all()
    return render(request, 'product/list.html'
            , {'productList': productList})

@login_required
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list_product')
    return render(request, 'product/form.html', {'form': form})

@login_required
def deleteProduct(request, pk):                    
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('/list_product')

@login_required
def updateProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/list_product')
    return render(request, 'product/form.html', {'form': form})