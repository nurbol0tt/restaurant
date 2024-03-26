from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.restaurant.models import Restaurant
from apps.restaurant.serializers import (
    RestaurantListSerializer,
    RestaurantDetailSerializer,
    RestaurantCreateSerializer,
)


class RestaurantViewSet(ViewSet):

    @swagger_auto_schema(request_body=RestaurantCreateSerializer)
    def create(self, request) -> Response:
        serializer = RestaurantCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], )
    def lists(self, request) -> Response:
        query = Restaurant.objects.all()
        serializer = RestaurantListSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None) -> Response:
        diary = get_object_or_404(Restaurant, id=pk)
        serializer = RestaurantDetailSerializer(diary)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(ViewSet):

    @swagger_auto_schema(request_body=RestaurantCreateSerializer)
    def create(self, request) -> Response:
        serializer = RestaurantCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def lists(self, request) -> Response:
        ...
