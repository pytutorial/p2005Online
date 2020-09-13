from rest_framework.response import Response
from rest_framework.views import APIView
#127.0.0.1:8000/api/hello
class HelloView(APIView):
    def get(self, request):
        return Response({'message': 'Hello'})

    def post(self, request):
        name = request.data.get('name', '')
        return Response({'message': 'Hello '+ name})
