import pandas as pd
from processing.data_cleaner import clean_orders


def make_raw_df():
    """A small fake raw dataset to test cleaning logic in isolation."""
    return pd.DataFrame({
        'order_id': ['ORD-1', 'ORD-1', 'ORD-2', 'ORD-3'],
        'warehouse': ['WH-A', 'WH-A', 'WH-B', 'WH-C'],
        'region': ['West', 'West', None, 'East'],
        'product': ['Router', 'Router', 'Laptop', 'Server'],
        'order_qty': [10, 10, 5, 20],
        'order_date': ['2026-01-01', '2026-01-01', '2026-01-05', '2026-02-01'],
        'delivery_date': ['2026-01-10', '2026-01-10', '2026-01-01', '2026-02-10'],
        'delivery_time_days': [9.0, 9.0, 999.0, None],
        'status': ['Delivered', 'Delivered', 'Pending', 'Delivered'],
    })


def test_removes_duplicate_rows():
    df = make_raw_df()
    cleaned = clean_orders(df)
    assert cleaned['order_id'].duplicated().sum() == 0


def test_drops_invalid_dates():
    df = make_raw_df()
    cleaned = clean_orders(df)
    # ORD-2 has delivery before order date, should be dropped
    assert 'ORD-2' not in cleaned['order_id'].values


def test_fills_missing_region():
    df = make_raw_df()
    cleaned = clean_orders(df)
    assert cleaned['region'].isnull().sum() == 0


def test_recomputes_delivery_time_days():
    df = make_raw_df()
    cleaned = clean_orders(df)
    row = cleaned[cleaned['order_id'] == 'ORD-1'].iloc[0]
    expected_days = (row['delivery_date'] - row['order_date']).days
    assert row['delivery_time_days'] == expected_days