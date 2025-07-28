from rest_framework import serializers
from .models import ProductType, Department, Vendor, Product
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
    
    def create(self, validated_data):
        raw_password = validated_data.pop('password') # remove and assigned password key and value which user sent and validated
        hash_password = make_password(raw_password) # hasing user's password using make_password function
        validated_data['password'] = hash_password # Assigning hashed password as a validated data
        return super().create(validated_data) # Passing the validated data to the parent class's create method to save the user instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
        