import pandas as pd
from processing.analytics import (
    status_distribution,
    warehouse_performance,
    regional_demand,
    delivery_variance,
    delay_tracking,
    product_analysis,
)


def make_clean_df():
    """A small fake cleaned dataset to test analytics functions in isolation."""
    return pd.DataFrame({
        'order_id': ['ORD-1', 'ORD-2', 'ORD-3', 'ORD-4'],
        'warehouse': ['WH-A', 'WH-A', 'WH-B', 'WH-B'],
        'region': ['West', 'West', 'East', 'East'],
        'product': ['Router', 'Laptop', 'Router', 'Server'],
        'order_qty': [10, 20, 5, 15],
        'delivery_time_days': [5, 10, 15, 20],
        'status': ['Delivered', 'Delayed', 'Delivered', 'Pending'],
    })


def test_status_distribution_sums_to_total_rows():
    df = make_clean_df()
    result = status_distribution(df)
    assert result.sum() == len(df)


def test_warehouse_performance_has_correct_columns():
    df = make_clean_df()
    result = warehouse_performance(df)
    assert 'total_orders' in result.columns
    assert 'avg_delivery_days' in result.columns
    assert result.loc['WH-A', 'total_orders'] == 2


def test_regional_demand_totals_match():
    df = make_clean_df()
    result = regional_demand(df)
    assert result['total_qty'].sum() == df['order_qty'].sum()


def test_delivery_variance_returns_expected_stats():
    df = make_clean_df()
    result = delivery_variance(df)
    assert result['min'] == 5
    assert result['max'] == 20


def test_delay_tracking_percentage_range():
    df = make_clean_df()
    result = delay_tracking(df)
    assert (result['delay_rate_pct'] >= 0).all()
    assert (result['delay_rate_pct'] <= 100).all()


def test_product_analysis_order_counts():
    df = make_clean_df()
    result = product_analysis(df)
    assert result.loc['Router', 'total_orders'] == 2