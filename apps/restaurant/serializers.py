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
        fields = ('rating', 'comment')


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'rating', 'comment')


class RestaurantDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = (
            'id', 'name', 'address', 'description', 'reviews'
        )


class RestaurantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            'name', 'address', 'description',
        )
