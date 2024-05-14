from rest_framework import generics,permissions
from . import serilizers
from . import models

# Create your views here.
# class VendorList(generics.ListAPIView):
class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serilizers.VendorSerializer
    # this is how we create view level permission to add project level simply add in settings.py
    # permission_classes=[permissions.IsAuthenticated]

# class VendorDetail(generics.RetrieveAPIView):
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serilizers.VendorDetailSerializer
    # permission_classes=[permissions.IsAuthenticated]
