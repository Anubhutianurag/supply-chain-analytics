import pandas as pd


def load_orders(filepath: str) -> pd.DataFrame:
    """Load raw supply chain orders CSV into a DataFrame."""
    df = pd.read_csv(filepath)
    return df