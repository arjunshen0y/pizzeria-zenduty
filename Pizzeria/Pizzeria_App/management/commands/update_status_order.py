from django.core.management.base import BaseCommand
from myapp.models import Order, Pizza, PizzaBase, Cheese, Toppings
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        now = timezone.now()
        one_minute_ago = now - timedelta(minutes=1)
        three_minutes_ago = now - timedelta(minutes=3)
        five_minutes_ago = now - timedelta(minutes=5)

        # Update orders based on time criteria
        Order.objects.filter(status='Placed', created_at__lte=one_minute_ago).update(status='Accepted')
        Order.objects.filter(status='Accepted', created_at__lte=three_minutes_ago).update(status='Preparing')
        Order.objects.filter(status='Preparing', created_at__lte=five_minutes_ago).update(status='Dispatched')
        Order.objects.filter(status='Dispatched', created_at__lte=five_minutes_ago).update(status='Delivered')


#A task to add sample pizzas

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Add your data creation logic here
        base = PizzaBase.objects.get(name='Thin Crust')
        cheese = Cheese.objects.get(name='Mozzarella')
        toppings = Toppings.objects.filter(name__in=['Pepperoni', 'Mushrooms', 'Onions', 'Olive', 'Bacon'])
        
        # Create a new pizza
        pizza = Pizza(
            base=base,
            cheese=cheese,
            quantity=2,
            pizza_price=12.99
        )
        pizza.save()
        pizza.toppings.set(toppings)

        self.stdout.write(self.style.SUCCESS('Successfully added pizza data'))
