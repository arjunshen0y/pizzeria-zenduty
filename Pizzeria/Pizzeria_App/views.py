from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

#Two simple api calls to add order and get the order details.
class AddOrderView(APIView): 
    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            pizza = serializer.save()
            return Response(PizzaSerializer(pizza).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)


