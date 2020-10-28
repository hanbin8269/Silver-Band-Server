from django.urls import include, path
from .views import LocationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]