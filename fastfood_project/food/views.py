from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, Order
from .permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from .throttling import CategoryThrottle, ProductThrottle, OrderThrottle

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [CategoryThrottle]

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [CategoryThrottle]

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [ProductThrottle]

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [ProductThrottle]

class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [OrderThrottle]

class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [OrderThrottle]

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to FastFood API!"})