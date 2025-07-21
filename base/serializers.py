from rest_framework import serializers
from .models import ProductType

class ProductTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'