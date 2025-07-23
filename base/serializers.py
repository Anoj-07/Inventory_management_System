from rest_framework import serializers
from .models import ProductType, Department

class ProductTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class DepartmentTypesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Department model.

    This serializer automatically generates fields for all attributes of the Department model,
    enabling serialization and deserialization of Department instances for API interactions.

    Attributes:
        Meta (class): Configuration for the serializer, specifying the model and fields to include.
    """
    class Meta:
        model = Department
        fields = '__all__'