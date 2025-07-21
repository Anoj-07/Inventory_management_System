from django.shortcuts import render
from .models import ProductType
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductTypesSerializer

# Create your views here.
# class  based views for ProductType

class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypesSerializer
