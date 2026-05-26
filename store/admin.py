from django.contrib import admin
from .models import Category, Product, ProductSize, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display        = ['name', 'slug']


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines             = [ProductSizeInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display        = ['name', 'category', 'price', 'stock', 'available', 'has_sizes']
    list_editable       = ['price', 'stock', 'available', 'has_sizes']
    list_filter         = ['category', 'available', 'has_sizes']
    search_fields       = ['name', 'description']


class OrderItemInline(admin.TabularInline):
    model           = OrderItem
    extra           = 0
    readonly_fields = ['product', 'size', 'quantity', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines         = [OrderItemInline]
    list_display    = ['id', 'user', 'status', 'payment_method', 'total_amount', 'created_at']
    list_editable   = ['status']
    list_filter     = ['status', 'payment_method', 'created_at']
    search_fields   = ['user__username', 'user__email']
    ordering        = ['-created_at']
    readonly_fields = ['user', 'total_amount', 'payment_method', 'created_at']