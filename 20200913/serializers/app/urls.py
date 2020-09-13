#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('hello', hello),
    path('get_product_detail/<pk>', getProductDetail),
    path('search_product', searchProduct),
]