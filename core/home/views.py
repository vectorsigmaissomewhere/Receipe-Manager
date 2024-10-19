from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReceipeSerializer 
from .models import Receipe, Ingredients

class ReceipeAPI(APIView):
    def get(self, request):
        queryset = Receipe.objects.all()
        print(queryset)
        serializer = ReceipeSerializer(queryset, many=True)
        print(serializer.data)
        return Response({
            "status": True,
            "message": "data fetched",
            "data": serializer.data
        })
