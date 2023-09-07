
# from datetime import datetime, timedelta
# from .models import Order 


# @app.task  # Schedule the task to run every 60 seconds (1 minute)
# def update_status_order(order_id):
#     try:
#         order = Order.objects.get(pk=order_id)
#         current_status = order.status

#         # Define status change logic here
#         if current_status == 'Placed':
#             order.status = 'Accepted'
#         elif current_status == 'Accepted':
#             order.status = 'Preparing'
#         elif current_status == 'Preparing':
#             order.status = 'Dispatched'
#         elif current_status == 'Dispatched':
#             order.status = 'Delivered'

#         order.save()
#     except Order.DoesNotExist:
#         pass
