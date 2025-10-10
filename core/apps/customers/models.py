from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities.customers import CustomerEntity


# Create your models here.
class CustomerModel(TimedBaseModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(
        max_length=11,
        verbose_name="Телефон",
        default=uuid4,
        unique=True,
    )
    token = models.CharField(max_length=255, verbose_name="Токен", unique=True)

    class Meta:
        db_table = "customers_customer"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.name

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            id=self.id,
            name=self.name,
            phone=self.phone,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
