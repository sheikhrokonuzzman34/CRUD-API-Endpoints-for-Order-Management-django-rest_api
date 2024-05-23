from django.urls import path
from .views import *

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('products/', product_list),
    path('products/<int:pk>/',product_detail),
    path('orders/',order_list),
    path('orders/<int:pk>/',order_detail),
]