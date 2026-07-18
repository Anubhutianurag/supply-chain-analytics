import pandas as pd
def status_distribution(df: pd.DataFrame) -> pd.Series:
    """Count of orders per status (Pending, Delivered, Delayed)."""
    return df['status'].value_counts()
def warehouse_performance(df: pd.DataFrame) -> pd.DataFrame:
    """Order count and average delivery time per warehouse."""
    return df.groupby('warehouse').agg(
        total_orders=('order_id', 'count'),
        avg_delivery_days=('delivery_time_days', 'mean')
    ).round(2)
def regional_demand(df: pd.DataFrame) -> pd.DataFrame:
    """Order count and total quantity ordered per region."""
    return df.groupby('region').agg(
        total_orders=('order_id', 'count'),
        total_qty=('order_qty', 'sum')
    ).sort_values('total_qty', ascending=False)
def delivery_variance(df: pd.DataFrame) -> pd.Series:
    """Descriptive stats (mean, std, min, max) for delivery_time_days."""
    return df['delivery_time_days'].agg(['mean', 'std', 'min', 'max']).round(2)
def delay_tracking(df: pd.DataFrame) -> pd.DataFrame:
    """Delay rate (%) per warehouse."""
    delay_rate = df.groupby('warehouse')['status'].apply(
        lambda x: (x == 'Delayed').mean() * 100
    ).round(2)
    return delay_rate.rename('delay_rate_pct').to_frame()
def product_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Order count, total quantity, and average delivery time per product."""
    return df.groupby('product').agg(
        total_orders=('order_id', 'count'),
        total_qty=('order_qty', 'sum'),
        avg_delivery_days=('delivery_time_days', 'mean')
    ).round(2).sort_values('total_orders', ascending=False)