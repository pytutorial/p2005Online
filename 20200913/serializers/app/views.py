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

@api_view(['POST'])
def createProduct(request):#127.0.0.1:8000/api/create_product
    data = request.data 
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    else:
        errors = serializer.errors
        return Response({'success': False, 'errors': errors})

@api_view(['PUT'])
def updateProduct(request, pk):#127.0.0.1:8000/api/update_product/1
    p = Product.objects.get(pk=pk)
    serializer = ProductSerializer(data=request.data, instance=p)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    else:
        errors = serializer.errors
        return Response({'success': False, 'errors': errors})

@api_view(['DELETE'])
def deleteProduct(request, pk):#127.0.0.1:8000/api/delete_product/1
    p = Product.objects.filter(pk=pk).first()   
    if p:
        p.delete()
        return Response({'success': True})
    else:
        return Response({'success': False,'error': 'Sản phẩm không tồn tại'})     