
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    payment_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_status = models.CharField(
        max_length=100, 
        choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed'), ('cancel', 'Cancel')], 
        default='pending'
    )
    payment_status = models.CharField(
        max_length=100, 
        choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], 
        default='unpaid'
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
     return f"Order by {self.user.username}, Total Amount: {self.total_amount}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
   
