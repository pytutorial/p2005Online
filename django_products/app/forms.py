from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
            
class OrderForm(forms.Form):            
    qty = forms.IntegerField(min_value=1)
    fullname = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)