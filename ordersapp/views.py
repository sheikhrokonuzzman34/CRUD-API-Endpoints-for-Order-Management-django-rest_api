from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status



# Product views
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

# Order views
class OrderList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order_data = serializer.validated_data
            # print(order_data)
            items_data = order_data.pop('orderitem_set', [])

            # Create the Order instance
            order = Order.objects.create(user=request.user, **order_data)
            
            # Create OrderItem instances
            for item_data in items_data:
                OrderItem.objects.create(
                    order=order,
                    product=item_data['product'],
                    quantity=item_data['quantity']
                )
            
            # Serialize the created order with its items
            result_serializer = OrderSerializer(order)
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        order = Order.objects.get(pk=pk, user=request.user)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            order_data = serializer.validated_data
            order_data.pop('items', None)
            for field, value in order_data.items():
                setattr(order, field, value)
            order.save()
            order.orderitem_set.all().delete()
            order_items_data = request.data.get('items')
            for item_data in order_items_data:
                OrderItem.objects.create(
                    order=order,
                    product_id=item_data['product'],
                    quantity=item_data['quantity']
                )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = Order.objects.get(pk=pk, user=request.user)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
