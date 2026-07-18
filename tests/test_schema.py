import pytest
from pydantic import ValidationError
from models.order_schema import Order


def test_valid_order_passes():
    order = Order(
        order_id='ORD-1000',
        warehouse='WH-C',
        region='West',
        product='Router',
        order_qty=42,
        order_date='2026-02-16',
        delivery_date='2026-03-24',
        delivery_time_days=36,
        status='Pending'
    )
    assert order.order_id == 'ORD-1000'
    assert order.order_qty == 42


def test_invalid_qty_raises_error():
    with pytest.raises(ValidationError):
        Order(
            order_id='ORD-9999',
            warehouse='WH-C',
            region='West',
            product='Router',
            order_qty='not-a-number',
            order_date='2026-02-16',
            delivery_date='2026-03-24',
            status='Pending'
        )


def test_missing_region_is_allowed():
    order = Order(
        order_id='ORD-1001',
        warehouse='WH-A',
        product='Laptop',
        order_qty=10,
        order_date='2026-01-01',
        delivery_date='2026-01-10',
        status='Delivered'
    )
    assert order.region is None