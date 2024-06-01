from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='orderitem_set')  # use the related_name if specified in the model

    class Meta:
        model = Order
        fields = ['id', 'user', 'payment_info', 'created_at', 'updated_at', 'delivery_status', 'payment_status', 'total_amount', 'items']
        read_only_fields = ['user']
