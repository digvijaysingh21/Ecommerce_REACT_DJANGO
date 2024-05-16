from urllib import request
from rest_framework import serializers
from . import models

# vendor serializer
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']

    def __init__(self, *args, **kwargs):
        super(VendorSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1

# vendor detail serializer
class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1

# Product list serialzier
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields=['id','category','vendor','title','detail','price']

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1


# Producty serializer
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields=['id','category','vendor','title','detail','price']

    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1

#Customer serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['id','user','mobile']

    def __init__(self, *args, **kwargs):
        super(CustomerSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

# customer detail serializer
class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['id','user','mobile']

    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1


# Order serilaizer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Order
        fields=['id','customer']

    def __init__(self, *args, **kwargs):
        super(OrderSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

# order detail serializer
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.OrderItems
        fields=['id','order','product']

    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1



