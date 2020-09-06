#app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('create_product', ProductCreateView.as_view()),
    path('hello', HelloView.as_view()),
]