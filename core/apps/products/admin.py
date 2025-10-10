from django.contrib import admin

from core.apps.products.models import (
    ProductModel,
    ReviewModel,
)


class ReviewInline(admin.TabularInline):
    model = ReviewModel
    extra = 1
    fk_name = "product"


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

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


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        ReviewModel.product.field.name,
        ReviewModel.customer.field.name,
        ReviewModel.rating.field.name,
        ReviewModel.comment.field.name,
    )

    list_select_related = (
        ReviewModel.product.field.name,
        ReviewModel.customer.field.name,
    )

    search_fields = (ReviewModel.product.field.name, ReviewModel.customer.field.name)
