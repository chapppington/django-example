from django.contrib.postgres.fields import ArrayField
from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import ProductEntity


class ProductModel(TimedBaseModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(blank=True, verbose_name="Описание товара")
    is_visible = models.BooleanField(
        default=True,
        verbose_name="Виден ли товар в каталоге",
    )

    tags = ArrayField(
        models.CharField(max_length=100),
        default=list,
        verbose_name="Теги",
    )

    class Meta:
        db_table = "products_product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
            tags=self.tags,
        )
