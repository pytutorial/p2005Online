from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User

@api_view(['POST'])
def createUser(request):
    username = request.data.get('username', '')
    password = request.data.get('password', '')
    password2 = request.data.get('password2', '')

    errors = []
    if not username:
        errors.append('Missing username.')

    if User.objects.filter(username=username).count() > 0:
        errors.append('User already exists.')    

    if not password:
        errors.append('Missing password.')

    if password and len(password) < 6:
        errors.append('Password needs to have at least 6 characters')

    if password.isdigit():
        errors.append('Password cannot be all digits')

    if password2 != password:
        errors.append('Wrong confirm password.')

    if len(errors) == 0:
        User.objects.create_user(username=username, password=password)
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': errors})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hello(request):         #127.0.0.1:8000/api/hello
    return Response({'message': 'Hello'})

class HelloView(APIView):   #127.0.0.1:8000/api/hello2
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message': 'Hello - 2'})    