from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'message': 'Welcome to Django API',
        'version': '1.0.0'
    })

def health(request):
    return JsonResponse({'status': 'OK'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('health/', health),
]
