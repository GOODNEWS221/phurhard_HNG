from django.urls import path
from django.http import JsonResponse
from .views import ProfileView

def api_root(request):
    return JsonResponse({"message": "Welcome to the API Home!"})

urlpatterns = [
    path('', api_root, name='api-root'),
    path('me/', ProfileView.as_view(), name='profile'),
]

