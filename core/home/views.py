from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReceipeSerializer, CreateReceipeSerializer
from .models import Receipe, Ingredients
import logging

logger = logging.getLogger(__name__)

class ReceipeAPI(APIView):
    def get(self, request):
        queryset = Receipe.objects.all()
        logger.debug(queryset)
        serializer = ReceipeSerializer(queryset, many=True)
        logger.debug(serializer.data)
        return Response({
            "status": True,
            "message": "Data fetched",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CreateReceipeSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": "Data not created",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        receipe = serializer.save()
        return Response({
            "status": True,
            "message": "Recipe created",
            "data": ReceipeSerializer(receipe).data  # Return serialized data
        }, status=status.HTTP_201_CREATED)

    def delete(self, request):
        data = request.data
        recipe_id = data.get('id')

        if not recipe_id:
            return Response({
                "status": False,
                "message": "ID not provided",
                "data": {}
            }, status=status.HTTP_400_BAD_REQUEST)

        receipe = Receipe.objects.filter(id=recipe_id)
        if receipe.exists():
            receipe.delete()
            return Response({
                "status": True,
                "message": "Recipe deleted",
                "data": {}
            }, status=status.HTTP_200_OK)

        return Response({
            "status": False,
            "message": "Recipe not found",
            "data": {}
        }, status=status.HTTP_404_NOT_FOUND)
