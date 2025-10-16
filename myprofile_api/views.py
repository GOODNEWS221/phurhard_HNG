import requests
from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_ratelimit.decorators import ratelimit
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ProfileView(APIView):
    def get(self, request):
        try:
            # Fetch random cat fact
            response = requests.get("https://catfact.ninja/fact", timeout=5)
            response.raise_for_status()
            cat_fact = response.json().get("fact", "Cats are cute beings!")
        except requests.RequestException:
            cat_fact = "Cat fact currently not available."

        # Create response data
        data = {
            "status": "success",
            "user": {
                "email": "goodnewsatekha@gmail.com", 
                "name": "Goodnews Atekha",        
                "stack": "Python/Django REST Framework"
            },
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "fact": cat_fact
        }

        return Response(data, status=status.HTTP_200_OK)
    


@api_view(['GET'])
@ratelimit(key='ip', rate='5/m', block=True)
def my_view(request):
    """Simple rate-limited endpoint"""
    return Response({"message": "Hello!"})


