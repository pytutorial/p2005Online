#app/views_users.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import OrderForm
def index(request):
    name = request.GET.get('name', '')
    productList = Product.objects.filter(name__contains=name)
    context = {'productList' : productList, 'name': name}
    return render(request, 'user/index.html', context)

def viewProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'user/view_product.html', context)

def orderProduct(request, pk):
    form = OrderForm()
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data) #TODO: SAVE to DB
            return redirect('/thank_you')
    context = {'product': product, 'form': form}
    return render(request, 'user/order_product.html', context)
