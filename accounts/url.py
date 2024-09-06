from django.urls import path  
from .views import *

urlpatterns = [  
    path('wallets/', Login.as_view(), name='walet-list-create'),
    path('wallets/<int:pk>/',Refresh.as_view(), name='walet-detail'),
]