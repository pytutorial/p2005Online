from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hello(request):         #127.0.0.1:8000/api/hello
    return Response({'message': 'Hello'})

class HelloView(APIView):   #127.0.0.1:8000/api/hello2
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message': 'Hello - 2'})    