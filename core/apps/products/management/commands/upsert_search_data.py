from django.core.management.base import BaseCommand

from core.apps.products.use_cases.search.upsert_search_data import (
    UpsertSearchDataUseCase,
)
from core.project.containers import get_container


class Command(BaseCommand):
    def handle(self, *args, **options) -> str | None:
        container = get_container()

        use_case = container.resolve(UpsertSearchDataUseCase)
        use_case.execute()
