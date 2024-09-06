from django.urls import path
from .views import Shoeordr, OrderCreateAPIView

urlpatterns = [
    path('orders/', Shoeordr.as_view(), name='order-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
]