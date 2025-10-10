from pydantic import (
    BaseModel,
    field_validator,
)


class ProductFilters(BaseModel):
    search: str | None = None

    @field_validator("search", mode="before")
    @classmethod
    def coerce_search_to_str_or_none(cls, v: object) -> str | None:
        if v is None or v == "":
            return None
        if isinstance(v, str):
            return v
        try:
            return str(v)
        except Exception:
            return None
