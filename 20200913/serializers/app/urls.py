#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('hello', hello),
    path('get_product_detail/<pk>', getProductDetail),
    path('search_product', searchProduct),
    path('create_product', createProduct),
    path('update_product/<pk>', updateProduct),
    path('delete_product/<pk>', deleteProduct),
]