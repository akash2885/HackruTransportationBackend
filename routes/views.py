from django.shortcuts import render
from rest_framework import viewsets
from .models import Routes
from .serializers import RouteSerializers


class RouteViewset(viewsets.ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RouteSerializers

# Create your views here.
