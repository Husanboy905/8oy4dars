from rest_framework import generics
from .models import Category, FoodItem, Order
from .serializers import CategorySerializer, FoodItemSerializer, OrderSerializer
from .permissions import CategoryPermission, FoodItemPermission, OrderPermission


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermission]


class FoodItemListCreateView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [FoodItemPermission]


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [OrderPermission]
