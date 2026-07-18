import matplotlib.pyplot as plt
import seaborn as sns

PALETTE = ['#7C3AED', '#EC4899', '#3B82F6', '#10B981', '#F59E0B']


def apply_style():
    """Apply consistent dark theme styling to all charts."""
    plt.rcParams['figure.facecolor'] = '#1A1D29'
    plt.rcParams['axes.facecolor'] = '#1A1D29'
    plt.rcParams['axes.edgecolor'] = '#2D3348'
    plt.rcParams['axes.labelcolor'] = '#FAFAFA'
    plt.rcParams['text.color'] = '#FAFAFA'
    plt.rcParams['xtick.color'] = '#9CA3AF'
    plt.rcParams['ytick.color'] = '#9CA3AF'
    plt.rcParams['grid.color'] = '#2D3348'
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3