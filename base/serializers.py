from rest_framework import serializers
from .models import ProductType, Department

class ProductTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class DepartmentTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'