from factory import Faker
from factory.django import DjangoModelFactory

from core.apps.products.models import ProductModel


class ProductModelFactory(DjangoModelFactory):
    title = Faker("first_name")
    description = Faker("text")
    is_visible = True

    class Meta:
        model = ProductModel
