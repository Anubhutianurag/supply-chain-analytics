import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from processing.analytics import delay_tracking
from visualizations.style import apply_style, PALETTE


def plot_delay_tracking(df: pd.DataFrame):
    """Bar chart of delay rate (%) per warehouse."""
    apply_style()
    data = delay_tracking(df)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=data.index, y=data['delay_rate_pct'], ax=ax, hue=data.index, palette=PALETTE, legend=False)
    ax.set_title('Delay Rate by Warehouse', color='#FAFAFA')
    ax.set_xlabel('Warehouse')
    ax.set_ylabel('Delay Rate (%)')

    return fig