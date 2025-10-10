from dataclasses import dataclass


@dataclass(frozen=True)
class ProductFiltersEntity:
    search: str | None = None
