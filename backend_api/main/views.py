from rest_framework import generics,permissions
from . import serilizers
from . import models

# Create your views here.

# Vendor views
# class VendorList(generics.ListAPIView):
class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serilizers.VendorSerializer
    # this is how we create view level permission to add project level simply add in settings.py
    # permission_classes=[permissions.IsAuthenticated]

# vendor detail views
# class VendorDetail(generics.RetrieveAPIView):
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serilizers.VendorDetailSerializer
    # permission_classes=[permissions.IsAuthenticated]

# Product views
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serilizers.ProductListSerializer

# product detail views
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serilizers.ProductDetailSerializer


# Customer
class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serilizers.CustomerSerializer
    # this is how we create view level permission to add project level simply add in settings.py
    # permission_classes=[permissions.IsAuthenticated]

# customer detail views
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serilizers.CustomerDetailSerializer
    # permission_classes=[permissions.IsAuthenticated]