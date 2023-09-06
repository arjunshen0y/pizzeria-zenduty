from rest_framework import serializers
from .models import Order,Toppings,Pizza, PizzaOrder

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toppings
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)
    class Meta:
        model = Pizza
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = '__all__'


