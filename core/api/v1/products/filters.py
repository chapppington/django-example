from pydantic import BaseModel


class ProductFilters(BaseModel):
    search: str | None = None
    
