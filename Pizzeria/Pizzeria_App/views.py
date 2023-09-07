from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer, PizzaSerializer
from django.utils import timezone
# from .tasks import update_status_order


class CreatePizzaView(APIView):
    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the pizza to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Two simple api calls to add order and get the order details.
class AddOrderView(APIView): 
    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            pizza = serializer.save()

            # Create an order for the pizza
            order = Order.objects.create()
            order.pizzas.add(pizza)

            # Schedule the task to update the order status
            # update_status_order.delay(order.id)
            return Response(PizzaSerializer(pizza).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class OrderDetailView(APIView):
#     def get(self, request, order_id):
#         try:
#             order = Order.objects.get(pk=order_id)
#             serializer = OrderSerializer(order)

#             elapsed_time = timezone.now() - order.created_at

#             if elapsed_time.total_seconds() >= 60:
#                 # If 1 minute has passed, change status to 'Accepted'
#                 order.status = 'Accepted'
#             elif elapsed_time.total_seconds() >= 120:
#                 # If 2 minutes have passed, change status to 'Preparing'
#                 order.status = 'Preparing'
#             elif elapsed_time.total_seconds() >= 300:
#                 # If 5 minutes have passed, change status to 'Dispatched'
#                 order.status = 'Dispatched'
#             elif elapsed_time.total_seconds() >= 480:
#                 # If 8 minutes have passed, change status to 'Delivered'
#                 order.status = 'Delivered'

#             order.save()

#             return Response(serializer.data)
#         except Order.DoesNotExist:
#             return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)


class UpdateOrderStatusView(APIView):
    def get(self, request, order_id):
        # Get all orders in "Placed" or "Accepted" status

        try:
            order = Order.objects.get(pk=order_id)
            orders = Order.objects.filter(status__in=["Placed", "Accepted"])

            for order in orders:
                
                elapsed_minutes = (timezone.now() - order.created_at).total_seconds() / 60

                
                if elapsed_minutes >= 1 and order.status == "Placed":
                    order.status = "Accepted"
                    order.save()
                elif elapsed_minutes >= 2 and order.status == "Accepted":
                    order.status = "Preparing"
                    order.save()
                elif elapsed_minutes >= 5 and order.status == "Preparing":
                    order.status = "Dispatched"
                    order.save()
                elif elapsed_minutes >= 10 and order.status == "Dispatched":
                    order.status = "Delivered"
                    order.save()
                

            return Response({"status": order.status})
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

class CheckOrderStatusView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id)
            return Response({"status": order.status})
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

# def place_order(request):
#     order = Order.objects.create(...)
#     update_status_order(order.id)

#     return render(request, 'order_placed.html', {'order': order})
