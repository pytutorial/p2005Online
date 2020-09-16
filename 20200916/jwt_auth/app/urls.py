#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('hello', hello),
    path('hello2', HelloView.as_view()),
    path('signup', createUser), #127.0.0.1:8000/api/signup
]