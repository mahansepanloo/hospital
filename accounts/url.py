from django.urls import path  
from .views import WaletListCreateView, WaletDetailView  

urlpatterns = [  
    path('wallets/', WaletListCreateView.as_view(), name='walet-list-create'),  
    path('wallets/<int:pk>/', WaletDetailView.as_view(), name='walet-detail'),  
]