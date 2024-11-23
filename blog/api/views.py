from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product, Order, OrderDetail
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, OrderDetailSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import Group

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        group = [group.name for group in user.groups.all()]
        return Response ({
            "username": user.username,
            "is_superuser" : user.is_superuser,
            "groups": group
        })


# ViewSet untuk Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# ViewSet untuk Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

# ViewSet untuk Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

# ViewSet untuk OrderDetail
class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

