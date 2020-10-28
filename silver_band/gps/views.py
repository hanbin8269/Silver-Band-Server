from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import LocationSerializer
from .models import Location


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()