# urls.py

from django.urls import path, include
from .views import OrderDetailView, AddOrderView

urlpatterns = [
    path('pizzapi/add_order/', AddOrderView.as_view(), name='add_order'),
    path('pizzapi/orders/<int:order_id>/', OrderDetailView.as_view(), name='order_info'),
]




