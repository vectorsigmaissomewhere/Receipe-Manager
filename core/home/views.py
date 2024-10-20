from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReceipeSerializer, CreateReceipeSerializer
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
    
    def post(self, request):
        data = request.data 
        serializer = CreateReceipeSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": "data not created",
                "data": serializer.errors
            })
        
        return Response({
            "status": True, 
            "message": "data created",
            "data": {}
        })
