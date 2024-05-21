import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainapp.models import Product, Order, OrderItem  # Adjust the import based on your actual models location

class Command(BaseCommand):
    help = 'Refresh the database and seed with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Command is being executed...")
        self.clear_database()
        self.stdout.write("Database cleared...")
        self.seed_database()
        self.stdout.write(self.style.SUCCESS('Successfully refreshed and seeded the database.'))

    def clear_database(self):
        self.stdout.write("Clearing OrderItems...")
        OrderItem.objects.all().delete()
        self.stdout.write("Clearing Orders...")
        Order.objects.all().delete()
        self.stdout.write("Clearing Products...")
        Product.objects.all().delete()

    def seed_database(self):
        self.stdout.write("Seeding Products...")
        product_names = [
            'Product 1', 'Product 2', 'Product 3', 
            'Product 4', 'Product 5', 'Product 6'
        ]
        products = []
        for name in product_names:
            product = Product.objects.create(
                name=name, 
                price=round(random.uniform(10.00, 100.00), 2)
            )
            products.append(product)
        
        self.stdout.write("Creating or getting dummy user...")
        user, created = User.objects.get_or_create(username='testuser', defaults={'password': 'password'})
        if created:
            self.stdout.write("Dummy user created.")
        else:
            self.stdout.write("Dummy user already exists.")

        self.stdout.write("Creating dummy orders...")
        for _ in range(5):
            order = Order.objects.create(
                user=user,
                total_amount=0,  # Update to total_amount
            )
            total_amount = 0  # Update to total_amount
            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                quantity = random.randint(1, 3)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                total_amount += product.price * quantity  # Update to total_amount
            
            order.total_amount = round(total_amount, 2)  # Update to total_amount
            order.save()

