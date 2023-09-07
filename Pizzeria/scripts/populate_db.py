import os
import django

# Set the DJANGO_SETTINGS_MODULE to the project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pizzeria.settings')  

# Configure Django
django.setup()

# Import your models and define data
from Pizzeria.models import Pizza  

def populate_pizzas():
    pizza_data = [
        {"base": "Thin-crust", "cheese": "Mozzarella", "toppings": "Pepperoni", "quantity": 2, "pizza_price": 12.99},
        {"base": "Normal", "cheese": "Cheddar", "toppings": "Mushrooms, Onions", "quantity": 1, "pizza_price": 10.99},
    ]

    for pizza_item in pizza_data:
        Pizza.objects.create(
            base=pizza_item["base"],
            cheese=pizza_item["cheese"],
            toppings=pizza_item["toppings"],
            quantity=pizza_item["quantity"],
            pizza_price=pizza_item["pizza_price"]
        )

if __name__ == '__main__':
    populate_pizzas()
