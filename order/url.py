from django.urls import path
from .views import OrdersViewSet



urlpatterns = [
    path('service',OrdersViewSet.as_view()),
]