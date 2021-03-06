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

@login_required
def listOrder(request):
    orderList = Order.objects.all()
    orderList = orderList.order_by('status', 'dateOrder')
    context = {'orderList': orderList}
    return render(request, 'order/list.html', context)

@login_required
def viewOrder(request, pk):
    order = Order.objects.get(pk=pk)    #get_object_or_404
    context = {'order': order}
    return render(request, 'order/detail.html', context)    

@login_required
def confirmOrder(request, pk):
    form = OrderConfirmForm()    
    if request.method == 'POST':
        form = OrderConfirmForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(pk=pk)
            order.status = Order.Status.DELIVERED
            order.deliverDate = form.cleaned_data['deliverDate']
            order.save()
            return redirect('/list_order')
    context = {'form': form}
    return render(request, 'order/confirm.html', context)

def cancelOrder(request, pk):
    if request.method == 'POST':
        order = Order.objects.get(pk=pk)
        order.status = Order.Status.CANCELED
        order.save()
        return redirect('/list_order')
    return render(request, 'order/cancel.html')    