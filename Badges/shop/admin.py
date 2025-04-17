from django.contrib import admin
from .models import Product, Purchase  # Убедитесь, что здесь нет лишних моделей

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('child_profile', 'product', 'quantity', 'total_price', 'purchase_date')