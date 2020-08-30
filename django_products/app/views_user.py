#app/views_users.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import OrderForm
from datetime import datetime

def index(request):
    name = request.GET.get('name', '')
    productList = Product.objects.filter(name__contains=name)
    context = {'productList' : productList, 'name': name}
    return render(request, 'user/index.html', context)

def viewProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'user/view_product.html', context)

def saveOrder(product, form_data):
    order = Order()
    order.product = product
    order.qty = form_data['qty']
    order.priceUnit = product.price
    order.fullname = form_data['fullname']
    order.phone = form_data['phone']
    order.address = form_data['address']
    order.dateOrder = datetime.now()
    order.status = Order.Status.PENDING
    order.save()

def orderProduct(request, pk):
    form = OrderForm(initial={'qty': 1})
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            saveOrder(product, form.cleaned_data)
            return redirect('/thank_you')
    context = {'product': product, 'form': form}
    return render(request, 'user/order_product.html', context)

def thankYou(request):
    return render(request, 'user/thank_you.html')