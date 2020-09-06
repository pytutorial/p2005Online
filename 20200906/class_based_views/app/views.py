from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from .models import Product
from .forms import ProductForm
#127.0.0.1:8000/create_product
class ProductCreateView(CreateView):
    #model = Product
    #fields = '__all__'
    #template_name = 'product_form.html'
    #success_url = '/'

    def get(self, request):
        form = ProductForm()
        return render(request, 'product_form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')   
        else:
             return render(request, 'product_form.html', {'form':form})    

# 127.0.0.1:8000/update_product/1
class ProductUpdateView(UpdateView):
    #model = Product
    #fields = '__all__'
    #template_name = 'product_form.html'
    #success_url = '/'

    def get(self, request, pk):
        p = Product.objects.get(pk=pk)
        form = ProductForm(instance=p)
        return render(request, 'product_form.html', {'form': form})

    def post(self, request, pk):
        p = Product.objects.get(pk=pk)
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'product_form.html', {'form': form})

# Create your views here.
def index(request):
    return render(request, 'index.html', {'productList': Product.objects.all()})

#127.0.0.1:8000/hello
class HelloView(View):    
    def get(self, request):
        context = {'name':'world'}
        return render(request, 'hello.html', context)

        
       
       