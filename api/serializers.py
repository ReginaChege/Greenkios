from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields= "__all__"
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields= "__all__"
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = "__all__"
class CartSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = "__all__"
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields ="__all__"
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Payment
        fields = "__all__"
class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields="__all__"        