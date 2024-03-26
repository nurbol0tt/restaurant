from rest_framework import serializers

from apps.restaurant.models import Restaurant
from apps.restaurant.models import Review


class RestaurantListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            'id', 'name', 'address', 'description',
        )


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('restaurant', 'rating', 'comment')


class RestaurantDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            'id', 'name', 'address', 'description',
        )


class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'name', 'address', 'description',
        )
