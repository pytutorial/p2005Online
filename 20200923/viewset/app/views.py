from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import viewsets
from .serializers import *
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #127.0.0.1:8000/api/product/search?keyword=IPhone
    @action(detail=False, methods=['get'])
    def search(self, request):
        keyword = request.GET.get('keyword', '')
        lst = Product.objects.filter(name__contains=keyword)
        data = ProductSerializer(lst,many=True).data
        return Response(data)

    #127.0.0.1:8000/api/product/2/get_price
    @action(detail=True, methods=['get'])
    def get_price(self, request, pk):
        p = Product.objects.get(pk=pk)
        return Response({'price': p.price})


@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})