from django.db import models
from background_task import background 
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class PizzaBase(models.Model):
    base_name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

class Cheese(models.Model):
    cheese_name = models.CharField(max_length=255)
    cheese_price = models.DecimalField(max_digits=10, decimal_places=2)

class Toppings(models.Model):
    topping_name = models.CharField(max_length=255)
    toppings_price = models.DecimalField(max_digits=10, decimal_places=2)

# class Pizza(models.Model):
#     base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE)
#     cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
#     toppings = models.ManyToManyField(Toppings)
#     quantity = models.PositiveIntegerField(default=1)
#     pizza_price = models.DecimalField(max_digits=10, decimal_places=2)

class Pizza(models.Model):
    base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Toppings)
    quantity = models.PositiveIntegerField(default=1)
    pizza_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"Pizza ({self.base}, {self.cheese}, {self.toppings.all()})"  # Customize the string representation

class Order(models.Model):
    STATUS_CHOICES = (
        ('Placed', 'Placed'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Placed')
    pizzas = models.ManyToManyField('Pizza', related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

class PizzaOrder(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=Order.STATUS_CHOICES, default='Placed')  
    last_status_change = models.DateTimeField(default=timezone.now) 

