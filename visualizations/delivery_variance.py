import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_delivery_variance(df: pd.DataFrame):
    """Histogram and boxplot showing the distribution of delivery times."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))

    sns.histplot(df['delivery_time_days'], bins=15, ax=axes[0])
    axes[0].set_title('Distribution of Delivery Times')
    axes[0].set_xlabel('Delivery Time (days)')
    axes[0].set_ylabel('Number of Orders')

    sns.boxplot(y=df['delivery_time_days'], ax=axes[1])
    axes[1].set_title('Delivery Time Spread')
    axes[1].set_ylabel('Delivery Time (days)')

    fig.tight_layout()
    return fig