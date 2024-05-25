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
    items = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'payment_info', 'created_at', 'updated_at', 'delivery_status', 'payment_status', 'total_amount', 'items']
        read_only_fields = ['user']

    def create(self, validated_data):
        items_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('orderitem_set')
        instance.payment_info = validated_data.get('payment_info', instance.payment_info)
        instance.delivery_status = validated_data.get('delivery_status', instance.delivery_status)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.save()

        # Update OrderItems
        instance.orderitem_set.all().delete()
        for item_data in items_data:
            OrderItem.objects.create(order=instance, **item_data)

        return instance
