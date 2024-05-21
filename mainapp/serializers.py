from rest_framework import serializers
from .models import Order, OrderItem, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product_data = item_data.pop('product')
            product, _ = Product.objects.get_or_create(**product_data)
            OrderItem.objects.create(order=order, product=product, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.user = validated_data.get('user', instance.user)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.save()

        for item_data in items_data:
            product_data = item_data.pop('product')
            product, _ = Product.objects.get_or_create(**product_data)
            order_item, created = OrderItem.objects.get_or_create(order=instance, product=product)
            order_item.quantity = item_data.get('quantity', order_item.quantity)
            order_item.save()

        return instance
