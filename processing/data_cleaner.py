import pandas as pd


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw supply chain orders data.

    Steps:
    1. Drop exact duplicate rows.
    2. Convert order_date/delivery_date to real datetime, strip time noise.
    3. Drop rows where delivery_date is before order_date (impossible, ~24% of data).
    4. Recompute delivery_time_days from the dates — original column was wrong
       in ~98% of rows, so it's dropped and replaced.
    5. Fill missing region with 'Unknown' (~3% missing, categorical — safer than guessing).
    6. Drop duplicates again post-filtering (a duplicate pair can split across
       the invalid-date filter, leaving a leftover single copy either way).
    """
    df = df.copy()

    # 1. Drop exact duplicate rows
    df = df.drop_duplicates()

    # 2. Convert to datetime, strip time-of-day noise
    df['order_date'] = pd.to_datetime(df['order_date']).dt.normalize()
    df['delivery_date'] = pd.to_datetime(df['delivery_date']).dt.normalize()

    # 3. Drop logically invalid rows (delivered before ordered)
    df = df[df['delivery_date'] >= df['order_date']]

    # 4. Recompute delivery_time_days from validated dates
    df['delivery_time_days'] = (df['delivery_date'] - df['order_date']).dt.days

    # 5. Fill missing region
    df['region'] = df['region'].fillna('Unknown')

    # 6. Final duplicate safety check
    df = df.drop_duplicates()

    return df.reset_index(drop=True)