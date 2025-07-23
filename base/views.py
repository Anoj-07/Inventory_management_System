from django.shortcuts import render
from .models import ProductType, Department
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductTypesSerializer, DepartmentTypesSerializer

# Create your views here.
# class  based views for ProductType

class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypesSerializer

class DepartmentTypeApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentTypesSerializer

