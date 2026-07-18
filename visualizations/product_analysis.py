import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from processing.analytics import product_analysis


def plot_product_analysis(df: pd.DataFrame):
    """Heatmap of order count, quantity, and avg delivery time per product."""
    data = product_analysis(df)
    # normalize each column to 0-1 so all three metrics are visually comparable
    # despite being on very different scales (orders ~20-30, qty ~500-700, days ~15-25)
    normalized = (data - data.min()) / (data.max() - data.min())

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(normalized, annot=data, fmt='.1f', cmap='YlGnBu', ax=ax, cbar=False)
    ax.set_title('Product Performance Heatmap')
    ax.set_xlabel('Metric')
    ax.set_ylabel('Product')

    return fig