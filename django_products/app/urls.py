from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('create_category', createCategory),
    path('update_category/<pk>', updateCategory), 
    path('delete_category/<pk>', deleteCategory), 
]