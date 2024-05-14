from rest_framework import generics
from . import serilizers
from . import models

# Create your views here.
class Vendorlist(generics.ListAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serilizers.VendorSerializer

