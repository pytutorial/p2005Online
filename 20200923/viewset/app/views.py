from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import *
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})