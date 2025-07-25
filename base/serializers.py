from rest_framework import serializers
from .models import ProductType, Department, Vendor, Product

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

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', queryset=ProductType.objects.all())
    departments = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Department.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

