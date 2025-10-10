from django.contrib import admin

from core.apps.customers.models import CustomerModel


@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        CustomerModel.name.field.name,
        CustomerModel.phone.field.name,
        CustomerModel.created_at.field.name,
        CustomerModel.updated_at.field.name,
    )

    search_fields = (CustomerModel.name.field.name, CustomerModel.phone.field.name)
