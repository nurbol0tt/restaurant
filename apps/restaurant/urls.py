from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from apps.restaurant.views import RestaurantViewSet, ReviewsViewSet

router = DefaultRouter()
router.register(r'restaurant', RestaurantViewSet, basename='restaurant')
router.register(r'reviews', ReviewsViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),

]
