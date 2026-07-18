import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from visualizations.style import apply_style, PALETTE


def plot_delivery_variance(df: pd.DataFrame):
    """Histogram and boxplot showing the distribution of delivery times."""
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))

    sns.histplot(df['delivery_time_days'], bins=15, ax=axes[0], color=PALETTE[0])
    axes[0].set_title('Distribution of Delivery Times', color='#FAFAFA')
    axes[0].set_xlabel('Delivery Time (days)')
    axes[0].set_ylabel('Number of Orders')

    sns.boxplot(y=df['delivery_time_days'], ax=axes[1], color=PALETTE[1])
    axes[1].set_title('Delivery Time Spread', color='#FAFAFA')
    axes[1].set_ylabel('Delivery Time (days)')

    fig.tight_layout()
    return fig