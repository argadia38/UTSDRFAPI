from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product, Order, OrderDetail
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, OrderDetailSerializer,UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from django.db import transaction



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
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
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
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# ViewSet untuk Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for order in queryset:
            order.username = order.user.username
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            # Get data from request
            data = request.data
            order_details = data.pop('order_details', [])

            # Create order
            order_serializer = self.get_serializer(data=data)
            order_serializer.is_valid(raise_exception=True)
            order = order_serializer.save()

            # Create order details
            for detail in order_details:
                detail['order'] = order.id_order
                detail_serializer = OrderDetailSerializer(data=detail)
                detail_serializer.is_valid(raise_exception=True)
                detail_serializer.save()

            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            
# ViewSet untuk OrderDetail
class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = OrderDetail.objects.all()
        order_id = self.request.query_params.get('order_id', None)
        if order_id is not None:
            queryset = queryset.filter(order__id_order=order_id)
        return queryset