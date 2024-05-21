from django.urls import path
from .views import *

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('orders/',order_list_create, name='order-list-create'),
    path('orders/<int:pk>/',order_detail, name='order-detail'),
    path('products/',product_list_create, name='product-list-create'),
]