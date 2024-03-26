import googlemaps
from rest_framework import serializers

from RestaurantPlatform import settings
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
    maps_url = serializers.SerializerMethodField()
    reviews = ReviewListSerializer(many=True)

    def get_maps_url(self, obj):
        gmaps = googlemaps.Client(settings.GOOGLE_MAPS_KEY)
        geocode_result = gmaps.geocode(obj.address)

        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return f"https://www.google.com/maps?q={location['lat']},{location['lng']}"
        return 'Unable to fetch location'

    class Meta:
        model = Restaurant
        fields = (
            'id', 'name', 'address', 'description', 'reviews', 'maps_url'
        )


class RestaurantReviewsDetailSerializer(serializers.ModelSerializer):
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
