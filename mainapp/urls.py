from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    
    path('orders/', order_list, name='order-list'),
    path('orders/<int:pk>/',order_detail, name='order-detail'),
]