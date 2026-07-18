import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from processing.analytics import product_analysis
from visualizations.style import apply_style


def plot_product_analysis(df: pd.DataFrame):
    """Heatmap of order count, quantity, and avg delivery time per product."""
    apply_style()
    data = product_analysis(df)
    normalized = (data - data.min()) / (data.max() - data.min())

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(normalized, annot=data, fmt='.1f', cmap='magma', ax=ax, cbar=False,
                annot_kws={'color': 'white'})
    ax.set_title('Product Performance Heatmap', color='#FAFAFA')
    ax.set_xlabel('Metric')
    ax.set_ylabel('Product')

    return fig