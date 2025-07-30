from django.shortcuts import render
from .models import ProductType, Department, Vendor, Product, Sell
from rest_framework.viewsets import (
    ModelViewSet,
    GenericViewSet,
)  # Modelviewset is used for already defiend CRUD operations and GenericViewSet is used for make own CRUD operations
from rest_framework.response import Response
from .serializers import (
    ProductTypesSerializer,
    DepartmentTypesSerializer,
    VendorSerializer,
    ProductSerializer,
    UserSerializer,
    LoginSerializer,
    SellSerializer,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .ai import create_description_with_ai
from django.db.models import Sum

# Create your views here.
# class  based views for ProductType


class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypesSerializer
    # permission_classes = [IsAuthenticated]  # permissions required for this view (Authentication and Authorization )


class DepartmentTypeApiView(GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentTypesSerializer  # This serializer will be used to serialize the Department model and for JSON serialization

    # Custom methods for DepartmentTypeApiView
    def list(self, request):
        queryset = self.get_queryset()  # It will get all the objects from the database
        serializer = self.get_serializer(
            queryset, many=True
        )  # It will serialize the queryset for JSON serialization object to JSON
        return Response(serializer.data)

    # Custom method to create a new department
    def create(self, request):
        serializer = self.get_serializer(
            data=request.data
        )  # it contain Json (request.data) # It will serialize the request data for JSON serialization object to JSON
        if serializer.is_valid(
            raise_exception=True
        ):  # It will validate the serializer data
            serializer.save()  # It will save the serializer data to the database
            return Response(
                serializer.data, status=201
            )  # It will return the serialized data and status code
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, pk):
        # try:
        #    query_set =  Department.objects.get(id=pk)
        # except:
        #     return Response({'error' : 'No matching data found!'}) # By default dictionary is converted onto json by Response class

        query_set = self.get_object()

        serializer = self.get_serializer(query_set, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        queryset = self.get_object()

        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk):
        queryset = self.get_object()  # get_object is used to
        queryset.delete()
        return Response()

    def partial_update(self, request, pk):
        query_set = self.get_object()

        serializer = self.get_serializer(query_set, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorApiView(GenericViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(
            raise_exception=True
        ):  # It will validate the serializer data
            serializer.save()  # It will save the serializer data to the database
            return Response(
                serializer.data, status=201
            )  # It will return the serialized data and status code
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, pk):
        query_set = self.get_object()

        serializer = self.get_serializer(query_set, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk):
        queryset = self.get_object()

        serilizer = self.get_serializer(queryset)
        return Response(serilizer.data)

    def destory(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        query_set = self.get_object()
        serilizer = self.get_serializer(query_set, data=request.data, partial=True)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_200_OK)
        else:
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellApiView(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer


class ProductApiView(ModelViewSet):
    # queryset = Product.objects.all().order_by('-stock') # descending according to stock (-) and with out (-) stock ascending order
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def best_selling(self, request):
        queryset = (
            Product.objects.all()
            .annotate(
                total_sell_quantity=Sum(
                    "sell__quantity"
                )  # to join sell and product and sell Quantity
            )
            .order_by("-total_sell_quantity")
        )  # kunai pani aauta field thapi dinxa annotate method le
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # API for Description Generator API
    def generate_description(self, request):
        product_name = request.data.get("name")

        if not product_name:
            return Response(
                {"error": "Product name is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            description = create_description_with_ai(product_name)
            return Response(
                {"name": product_name, "generated_description": description},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserApiView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        []
    )  # No permissions required for this view (Authentication and Authorization ) # it don't take defult permission class from settings.py

    # For register
    def register(self, request):

        serializer = self.get_serializer(
            data=request.data
        )  # It will serialize the request data for JSON serialization object to JSON

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # for Login
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if (
            serializer.is_valid()
        ):  # Validate whether user informatiioin being sent or not
            username = request.data.get("username")
            password = request.data.get("password")

            user = authenticate(
                username=username, password=password
            )  # Authenticate the user # Passing username and password in authentication to check whether it matches with any user or not if mathched it returns user object data if not it returns None
            if user == None:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )  # we send data in dictionary format and it will be converted to JSON by Response class and you cannot return object directly
            else:
                token, _ = Token.objects.get_or_create(
                    user=user
                )  # It will get already having token or create new if there is none # it will give in tuple (get_or_create)
                # token,_ here it is like a,b = (1, 3)
                return Response({"token": token.key})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
