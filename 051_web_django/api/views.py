from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Welcome to Django REST API',
        'version': '1.0.0',
        'endpoints': {
            'todos': '/api/todos/',
            'admin': '/admin/'
        }
    })

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
