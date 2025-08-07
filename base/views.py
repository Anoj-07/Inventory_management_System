from django.shortcuts import render
from .models import ProductType, Department, Vendor, Product, Rating, Sell, Purchase
from rest_framework.viewsets import (
    ModelViewSet,
    GenericViewSet,
    ReadOnlyModelViewSet
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
    PurchaseSerializer,
    RatingSerializer,
    GroupSerializer
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .ai import create_description_with_ai
from django.db.models import Sum, Avg
from rest_framework.exceptions import APIException

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

    # Override perform_create to update stock after selling
    def perform_create(self, serializer):
        # Save the Sell object first
        sell_instance = serializer.save()

        # Get the product related to this sell
        product = sell_instance.product  
        sell_quantity = sell_instance.quantity  

        # Check if enough stock is available before selling
        if product.stock < sell_quantity:
            raise APIException("Not enough stock available to sell!")

        # Decrease stock after sale
        product.stock -= sell_quantity
        product.save()

    # Override perform_update to handle stock changes if quantity is updated
    def perform_update(self, serializer):
        old_instance = self.get_object()  
        old_quantity = old_instance.quantity  

        sell_instance = serializer.save()
        new_quantity = sell_instance.quantity  

        product = sell_instance.product  

        # Adjust stock based on quantity change
        quantity_diff = new_quantity - old_quantity

        if quantity_diff > 0:  # Selling more
            if product.stock < quantity_diff:
                raise APIException("Not enough stock to increase sale quantity!")
            product.stock -= quantity_diff
        else:  # Selling less (return case)
            product.stock += abs(quantity_diff)

        product.save()


class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    # Override perform_create to increase stock after purchase
    def perform_create(self, serializer):
        purchase_instance = serializer.save()
        product = purchase_instance.product
        purchase_quantity = purchase_instance.quantity

        # Increase stock after purchase
        product.stock += purchase_quantity
        product.save()

    # Override perform_update to handle quantity changes
    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_quantity = old_instance.quantity

        purchase_instance = serializer.save()
        new_quantity = purchase_instance.quantity

        product = purchase_instance.product

        # To Adjust stock
        quantity_diff = new_quantity - old_quantity
        product.stock += quantity_diff
        product.save()



class ProductApiView(ModelViewSet):
    # queryset = Product.objects.all().order_by('-stock') # descending according to stock (-) and with out (-) stock ascending order
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]  # this is for permission

    """
    => (perform_create() is not an API view method that returns responses.)
    # perform_create() is a hook method that DRF provides in class-based views (like ModelViewSet), which is called automatically when .create() is called on the view (i.e., during a POST request).
    """
    # TO Generte Description form AI
    def perform_create(self, serializer):  
        product_name = serializer.validated_data.get("name")
        description = serializer.validated_data.get("description", None)

        # 💡 If description is not provided, generate it
        try:
            if not description:
                description = create_description_with_ai(product_name)

            serializer.save(description=description)

        except Exception as e:
        # Raise DRF exception, which sends proper HTTP 500 response
            raise APIException(f"AI generation failed: {str(e)}")


    # Best selling
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

    # most purchased
    def most_purchased(self, request):
        queryset = (
            Product.objects.all()
            .annotate(total_purchase_quantity=Sum("purchase__quantity"))
            .order_by("-total_purchase_quantity")
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # rating
    def top_rated(self, request):
        queryset = (
            Product.objects.all()
            .annotate(avg_rating=Avg("ratings__rating"))
            .order_by("-avg_rating")
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def generate_description(self, request):
    #     product_id = request.data.get("id")

    #     if not product_id:
    #         return Response(
    #             {"error": "Product ID is required."},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )

    #     try:
    #         # Fetch the product
    #         product = Product.objects.get(id=product_id)

    #         # Use the AI function to generate a description based on product name
    #         generated_description = create_description_with_ai(product.name)

    #         # Save the generated description to the product
    #         product.description = generated_description
    #         product.save()

    #         return Response({
    #             "id": product.id,
    #             "name": product.name,
    #             "generated_description": generated_description,
    #             "message": "Product description updated successfully"
    #         }, status=status.HTTP_200_OK)

    #     except Product.DoesNotExist:
    #         return Response(
    #             {"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND
    #         )

    #     except Exception as e:
    #         return Response(
    #             {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #         )


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

class GroupApiView(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RatingApiView(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
