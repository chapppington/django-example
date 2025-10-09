from django.contrib import admin

from core.apps.products.models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        ProductModel.title.field.name,
        ProductModel.is_visible.field.name,
        ProductModel.description.field.name,
        ProductModel.created_at.field.name,
        ProductModel.updated_at.field.name,
    )

    list_filter = (
        ProductModel.is_visible.field.name,
        ProductModel.created_at.field.name,
        ProductModel.updated_at.field.name,
    )

    search_fields = (ProductModel.title.field.name, ProductModel.description.field.name)
