import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from processing.analytics import warehouse_performance
from visualizations.style import apply_style, PALETTE


def plot_warehouse_performance(df: pd.DataFrame):
    """Bar chart of average delivery time per warehouse."""
    apply_style()
    data = warehouse_performance(df)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=data.index, y=data['avg_delivery_days'], ax=ax, hue=data.index, palette=PALETTE, legend=False)
    ax.set_title('Average Delivery Time by Warehouse', color='#FAFAFA')
    ax.set_xlabel('Warehouse')
    ax.set_ylabel('Avg Delivery Time (days)')

    return fig