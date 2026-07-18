from pydantic import BaseModel
from typing import Optional
from datetime import date


class Order(BaseModel):
    order_id: str
    warehouse: str
    region: Optional[str] = None
    product: str
    order_qty: int
    order_date: date
    delivery_date: date
    delivery_time_days: Optional[float] = None
    status: str