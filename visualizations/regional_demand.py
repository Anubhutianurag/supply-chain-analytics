import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from processing.analytics import regional_demand


def plot_regional_demand(df: pd.DataFrame):
    """Bar chart of total quantity ordered per region."""
    data = regional_demand(df)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=data.index, y=data['total_qty'], ax=ax)
    ax.set_title('Total Quantity Ordered by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Quantity')

    return fig