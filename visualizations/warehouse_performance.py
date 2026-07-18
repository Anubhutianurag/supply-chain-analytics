import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from processing.analytics import warehouse_performance


def plot_warehouse_performance(df: pd.DataFrame):
    """Bar chart of average delivery time per warehouse."""
    data = warehouse_performance(df)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=data.index, y=data['avg_delivery_days'], ax=ax)
    ax.set_title('Average Delivery Time by Warehouse')
    ax.set_xlabel('Warehouse')
    ax.set_ylabel('Avg Delivery Time (days)')

    return fig