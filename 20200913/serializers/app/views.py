from rest_framework.response import Response
from rest_framework.decorators import api_view
#127.0.0.1:8000/api/hello
@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

from .serializers import *

#127.0.0.1:8000/api/get_product_detail/1
@api_view(['GET'])
def getProductDetail(request, pk):
    p = Product.objects.get(pk=pk)
    data = ProductSerializer(p).data
    return Response(data)