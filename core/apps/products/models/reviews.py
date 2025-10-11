from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.customers.models import CustomerModel
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.models import ProductModel


class ReviewModel(TimedBaseModel):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        verbose_name="Товар",
        related_name="product_reviews",
    )
    customer = models.ForeignKey(
        CustomerModel,
        on_delete=models.CASCADE,
        verbose_name="Клиент",
        related_name="customer_reviews",
    )

    rating = models.PositiveSmallIntegerField(verbose_name="Рейтинг", default=1)
    comment = models.TextField(verbose_name="Текст отзыва", blank=True, default="")

    def __str__(self):
        return f"Отзыв от {self.customer} на {self.product} (рейтинг: {self.rating})"

    class Meta:
        db_table = "reviews"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ("product", "customer")

    # TODO принимать только review
    @classmethod
    def from_entity(
        cls,
        review: ReviewEntity,
        product: ProductEntity,
        customer: CustomerEntity,
    ) -> "ReviewModel":
        return cls(
            id=review.id,
            product_id=product.id,
            customer_id=customer.id,
            rating=review.rating,
            comment=review.comment,
        )

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            id=self.id,
            rating=self.rating,
            comment=self.comment,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
