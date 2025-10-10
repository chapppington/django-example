from dataclasses import dataclass
from datetime import datetime


@dataclass
class CustomerEntity:
    id: int
    name: str
    phone: str
    created_at: datetime
    updated_at: datetime
