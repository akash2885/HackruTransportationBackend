from django.shortcuts import render
from rest_framework import viewsets
from .models import Fuel
from .serializer import FuelSerializer


class FuelViewset(viewsets.ModelViewSet):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer

# Create your views here.
