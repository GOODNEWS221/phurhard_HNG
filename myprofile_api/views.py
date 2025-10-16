from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from datetime import datetime, timezone

@api_view(['GET'])
def me(request):
    try:
        response = requests.get('https://catfact.ninja/fact', timeout=5)
        cat_fact = response.json().get('fact', 'Cat fact not available.')
    except Exception:
        cat_fact = "Fact about cats currently not available."

    data = {
        "status": "success",
        "user": {
            "email": "your_email@example.com",
            "name": "Goodnews Atekha",
            "stack": "Python/Django REST Framework"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return Response(data)


