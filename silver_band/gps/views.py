from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LocationSerializer
from .models import Location


class LocationViewSet(viewsets.ViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()