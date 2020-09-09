from rest_framework.response import Response
from rest_framework.decorators import api_view

#127.0.0.1:8000/api/hello
@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

productList = [
    { 'id': 1, 'code': 'IPX', 'name': 'Iphone X'},
    { 'id': 2, 'code': 'IP8', 'name': 'Iphone 8'},
]    

#127.0.0.1:8000/api/search_product?keyword=Iphone 8
@api_view(['GET'])
def searchProduct(request):
    keyword = request.GET.get('keyword', '')
    result = [p for p in productList if keyword in p['name']]
    return Response(result)

#127.0.0.1:8000/api/get_product_detail/1
@api_view(['GET'])
def getProductDetail(request, pk):
    for p in productList:
        if str(p['id']) == pk:
            return Response(p)
    return Response({'error': 'Not found'})

#127.0.0.1:8000/api/create_product
@api_view(['POST'])
def createProduct(request):
    data = request.data 
    code = data.get('code')
    name = data.get('name')
    next_id = productList[-1]['id'] + 1 if productList else 1
    productList.append({'id': next_id, 'code': code, 'name': name})
    return Response({'success': True})

#127.0.0.1:8000/api/update_product/1
@api_view(['PUT'])
def updateProduct(request, pk):
    data = request.data
    for p in productList:
        if str(p['id'] == pk):
            p.update(data)    
            return Response({'success': True})
    return Response({'success': False, 'error': 'Not found'})

#127.0.0.1:8000/api/delete_product/1
@api_view(['DELETE'])
def deleteProduct(request, pk):
    global productList
    productList = [p for p in productList if str(p['id']) != pk]
    return Response({'success': True})
