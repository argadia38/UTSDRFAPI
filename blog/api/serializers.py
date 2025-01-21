from rest_framework import serializers
from .models import Category, Product, Order, OrderDetail
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    nameCategory = serializers.CharField(source='category.name', read_only=True)
        
    class Meta:
        model = Product
        fields = '__all__'

# OrderDetailSerializer harus didefinisikan sebelum OrderSerializer
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.CharField(source='user.username', read_only=True)
    order_details = OrderDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'