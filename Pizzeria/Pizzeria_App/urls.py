# urls.py

from django.urls import path, include
from .views import AddOrderView, CreatePizzaView, CheckOrderStatusView, UpdateOrderStatusView

urlpatterns = [
    path('add_pizza/', CreatePizzaView.as_view(), name='create-pizza'),
    path('add_order/', AddOrderView.as_view(), name='add_order'),
    
    path('order_status/<int:order_id>/', UpdateOrderStatusView().as_view(), name='order_status')
]




