from django.contrib import admin
from core.apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        Product.title.field.name, 
        Product.is_visible.field.name, 
        Product.description.field.name, 
        Product.created_at.field.name, 
        Product.updated_at.field.name
    )
    
    list_filter = (
        Product.is_visible.field.name, 
        Product.created_at.field.name, 
        Product.updated_at.field.name
    )
    
    search_fields = (
        Product.title.field.name, 
        Product.description.field.name
    )
