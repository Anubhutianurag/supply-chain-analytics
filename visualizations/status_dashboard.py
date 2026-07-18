import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from processing.analytics import status_distribution


def plot_status_distribution(df: pd.DataFrame):
    """Bar chart of order counts per status."""
    data = status_distribution(df)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=data.index, y=data.values, ax=ax)
    ax.set_title('Order Status Distribution')
    ax.set_xlabel('Status')
    ax.set_ylabel('Number of Orders')

    return fig