"""
URL configuration for inventory_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from base.views import (
    ProductTypeApiView,
    DepartmentTypeApiView,
    VendorApiView,
    ProductApiView,
    UserApiView,
    SellApiView,
    PurchaseApiView,
    RatingApiView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("product/types/", ProductTypeApiView.as_view({"get": "list", "post": "create"})
    ),
    path("product/types/<int:pk>/",
        ProductTypeApiView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),


    path("department/types/",
        DepartmentTypeApiView.as_view({"get": "list", "post": "create"}),
    ),
    path("department/types/<int:pk>",
        DepartmentTypeApiView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),


    path("vendor/", VendorApiView.as_view({"get": "list", "post": "create"})),
    path("vendor/<int:pk>/",
        VendorApiView.as_view(
            {
                "get": "retrive",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),


    path("product/", ProductApiView.as_view({"get": "list", "post": "create"})),
    path("best/selling/product/", ProductApiView.as_view({"get": "best_selling"})),
    path("product/<int:pk>/",
        ProductApiView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),


    path("register/", UserApiView.as_view({"post": "register"})),
    path("login/", UserApiView.as_view({"post": "login"})),


    path("sell/", SellApiView.as_view({"get": "list", "post": "create"})),
    path("sell/<int:pk>/",
        SellApiView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),


    path("rating/", SellApiView.as_view({"get": "list", "post": "create"})),
    path("rating/<int:pk>/",
        SellApiView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),


    path("purchase/", PurchaseApiView.as_view({"get": "list", "post": "create"})),
    path("most/purchased/products/", ProductApiView.as_view({"get": "most_purchased"})),
    path("purchase/<int:pk>/",
        PurchaseApiView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),


    path("generate-ai/", ProductApiView.as_view({"post": "generate_description"})),
]
