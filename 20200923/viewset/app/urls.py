from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
urlpatterns = [path('hello', hello),]
router = DefaultRouter()
router.register('product', ProductViewSet)
urlpatterns += router.urls
#127.0.0.1:8000/api/product : GET --> list, POST -> new
#127.0.0.1:8000/api/product/1 : GET --> detail, PUT --> update, DELETE -->delete