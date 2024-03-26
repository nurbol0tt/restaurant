from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from apps.restaurant.views import RestaurantViewSet

router = DefaultRouter()
router.register(r'patients', RestaurantViewSet, basename='patient')

urlpatterns = [
    path('', include(router.urls)),

]
