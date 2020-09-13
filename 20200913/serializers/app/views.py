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

#127.0.0.1:8000/api/search_product?keyword=IPhone+X
@api_view(['GET'])
def searchProduct(request):
    keyword = request.GET.get('keyword', '')
    result = Product.objects.filter(name__icontains=keyword)
    data = ProductSerializer(result, many=True).data
    return Response(data)