from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hello(request):#127.0.0.1:8000/api/hello
    return Response({'message': 'Hello'})