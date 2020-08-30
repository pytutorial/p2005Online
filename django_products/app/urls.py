from django.urls import path
from .views import *
from .views_user import *

urlpatterns = [
    #==================User===================
    path('', index),
    path('view_product/<pk>', viewProduct),
    path('order_product/<pk>', orderProduct),
    path('thank_you', thankYou),
    #==================Staff==================

    path('staff', listCategory),
    path('create_category', createCategory),
    path('update_category/<pk>', updateCategory), 
    path('delete_category/<pk>', deleteCategory), 

    path('list_product', listProduct),
    path('create_product', createProduct),
    path('update_product/<pk>', updateProduct), 
    path('delete_product/<pk>', deleteProduct),
]