from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order, OrderDetail

# Register your models here.

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
    search_fields = ('name', 'description', 'category__name')
    list_filter = ('category', 'created_at', 'updated_at')
    ordering = ('id_product',)
    autocomplete_fields = ('category',)

# Admin untuk Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id_order', 'user', 'order_date', 'total_price', 'status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at', 'updated_at')
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
