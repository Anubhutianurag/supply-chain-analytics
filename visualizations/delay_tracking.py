import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from processing.analytics import delay_tracking


def plot_delay_tracking(df: pd.DataFrame):
    """Bar chart of delay rate (%) per warehouse."""
    data = delay_tracking(df)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=data.index, y=data['delay_rate_pct'], ax=ax)
    ax.set_title('Delay Rate by Warehouse')
    ax.set_xlabel('Warehouse')
    ax.set_ylabel('Delay Rate (%)')

    return fig