from django.urls import path  
from .views import (
    ServiceListAPIView,
    ServiceDetailAPIView,
    ServiceCreateAPIView,
    ServiceUpdateAPIView,
    ServiceDeleteAPIView,
    CatListAPIView,
    CatDetailAPIView,
    CatCreateAPIView,
    CatUpdateAPIView,
    CatDeleteAPIView,
)

urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('services/create/', ServiceCreateAPIView.as_view(), name='service-create'),
    path('services/update/<int:pk>/', ServiceUpdateAPIView.as_view(), name='service-update'),
    path('services/delete/<int:pk>/', ServiceDeleteAPIView.as_view(), name='service-delete'),

    path('categories/', CatListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CatDetailAPIView.as_view(), name='category-detail'),
    path('categories/create/', CatCreateAPIView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', CatUpdateAPIView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CatDeleteAPIView.as_view(), name='category-delete'),
]