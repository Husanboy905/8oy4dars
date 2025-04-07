
from django.urls import path
from .views import CategoryListCreateView, FoodItemListCreateView, OrderListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('foods/', FoodItemListCreateView.as_view(), name='food-list'),
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
]
