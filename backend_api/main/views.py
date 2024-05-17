from rest_framework import generics,permissions,pagination,viewsets
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
    # pagination_class=pagination.LimitOffsetPagination
    pagination_class=pagination.PageNumberPagination

# product detail views
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serilizers.ProductDetailSerializer


# Customer
class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serilizers.CustomerSerializer
   

# customer detail views
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serilizers.CustomerDetailSerializer

# Order
class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serilizers.OrderSerializer

class OrderDetail(generics.ListAPIView):
    # queryset = models.OrderItems.objects.all()
    serializer_class = serilizers.OrderDetailSerializer

# over ride query set
    def get_queryset(self):
        order_id=self.kwargs['pk']
        order=models.Order.objects.get(id=order_id)
        order_items=models.OrderItems.objects.filter(order=order)
        return order_items

  
class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class=serilizers.CustomerAddressSerilaizer
    queryset=models.CustomerAddress.objects.all()

    
class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class=serilizers.ProductRatingSerilaizer
    queryset=models.ProductRating.objects.all()

    