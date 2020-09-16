#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('hello', hello),
    path('hello2', HelloView.as_view()),
]