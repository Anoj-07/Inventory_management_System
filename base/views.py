from django.shortcuts import render
from .models import ProductType, Department
from rest_framework.viewsets import ModelViewSet, GenericViewSet # Modelviewset is used for already defiend CRUD operations and GenericViewSet is used for make own CRUD operations
from rest_framework.response import Response
from .serializers import ProductTypesSerializer, DepartmentTypesSerializer

# Create your views here.
# class  based views for ProductType

class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypesSerializer

class DepartmentTypeApiView(GenericViewSet):
    queryset = Department.objects.all() 
    serializer_class = DepartmentTypesSerializer # This serializer will be used to serialize the Department model and for JSON serialization

    # Custom methods for DepartmentTypeApiView
    def list(self, request):
        queryset = self.get_queryset() # It will get all the objects from the database
        serializer = self.get_serializer(queryset, many=True) # It will serialize the queryset for JSON serialization object to JSON
        return Response(serializer.data)
    
    # Custom method to create a new department
    def create(self, request):
        serializer = self.get_serializer(data=request.data)# it contain Json (request.data) # It will serialize the request data for JSON serialization object to JSON
        if serializer.is_valid(raise_exception=True): # It will validate the serializer data
            serializer.save() # It will save the serializer data to the database
            return Response(serializer.data, status=201) # It will return the serialized data and status code
        else:
            return Response(serializer.errors, status=400)
