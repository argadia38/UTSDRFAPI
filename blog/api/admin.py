from django.contrib import admin
from .models import Category, Product, Order, OrderDetail
from django.contrib.auth.models import User

# Admin untuk Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id_category', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('id_category',)

# Admin untuk Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id_product', 'name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category__name', 'size')
    list_filter = ('category', 'created_at', 'updated_at')
    ordering = ('id_product',)
    autocomplete_fields = ('category',)

# Admin untuk Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id_order', 'user', 'order_date', 'total_price',)
    search_fields = ('user__username',)  # Perbaikan, menjadikannya tuple
    list_filter = ('order_date', 'user',)  # Menambahkan lebih banyak filter
    ordering = ('id_order',)
    autocomplete_fields = ('user',)

# Admin untuk OrderDetail
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id_detail', 'order', 'product', 'quantity', 'price', 'created_at', 'updated_at')
    search_fields = ('order__id_order', 'product__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('id_detail',)
    autocomplete_fields = ('order', 'product')
