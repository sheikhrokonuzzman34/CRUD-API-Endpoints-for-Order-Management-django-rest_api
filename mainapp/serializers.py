from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source='orderitem_set', many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_items', 'total_price', 'payment_information', 'created_at', 'updated_at']

    def create(self, validated_data):
        order_items_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        total_price = 0
        for order_item_data in order_items_data:
            product = order_item_data['product']
            quantity = order_item_data['quantity']
            order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)
            total_price += product.price * quantity
        order.total_price = total_price
        order.save()
        return order