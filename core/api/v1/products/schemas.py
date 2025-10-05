from pydantic import BaseModel
from datetime import datetime


class ProductSchema(BaseModel):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None
    

ProductListSchema = list[ProductSchema]
    
