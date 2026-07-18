import streamlit as st

from config.settings import RAW_DATA_PATH, PAGE_TITLE, PAGE_ICON, LAYOUT
from processing.data_loader import load_orders
from processing.data_cleaner import clean_orders
from visualizations.status_dashboard import plot_status_distribution
from visualizations.warehouse_performance import plot_warehouse_performance
from visualizations.regional_demand import plot_regional_demand
from visualizations.delivery_variance import plot_delivery_variance
from visualizations.delay_tracking import plot_delay_tracking
from visualizations.product_analysis import plot_product_analysis

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)

# --- Custom CSS ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #7C3AED, #EC4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        color: #9CA3AF;
        font-size: 1rem;
        margin-top: 0;
        margin-bottom: 1.5rem;
    }
    [data-testid="stMetric"] {
        background: #1A1D29;
        border: 1px solid #2D3348;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    [data-testid="stMetricLabel"] {
        color: #9CA3AF;
    }
    .chart-container {
        background: #1A1D29;
        border: 1px solid #2D3348;
        border-radius: 16px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    section[data-testid="stSidebar"] {
        background: #14161F;
    }
    @keyframes roam {
        0%   { left: -5%; }
        50%  { left: 95%; transform: scaleX(1); }
        50.01% { transform: scaleX(-1); }
        100% { left: -5%; transform: scaleX(-1); }
    }
    .panda {
        position: fixed;
        top: 55px;
        font-size: 2.5rem;
        animation: roam 18s linear infinite;
        z-index: 9999;
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="panda">🐼</div>', unsafe_allow_html=True)

st.markdown(f'<p class="main-header">{PAGE_ICON} Supply Chain Analytics</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Cleaned, validated order data across warehouses, regions, and products.</p>', unsafe_allow_html=True)


@st.cache_data
def get_cleaned_data():
    df = load_orders(RAW_DATA_PATH)
    return clean_orders(df)


df = get_cleaned_data()

# --- Metrics ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("📦 Total Orders", len(df))
col2.metric("⏱️ Avg Delivery Time", f"{df['delivery_time_days'].mean():.1f} days")
delayed_pct = (df['status'] == 'Delayed').mean() * 100
col3.metric("⚠️ Delay Rate", f"{delayed_pct:.1f}%")
col4.metric("🌍 Regions Covered", df['region'].nunique())

st.write("")

# --- Sidebar ---
st.sidebar.markdown("### 📊 Dashboards")
view = st.sidebar.radio(
    "Select a view",
    [
        "📈 Status Distribution",
        "🏭 Warehouse Performance",
        "🗺️ Regional Demand",
        "📦 Delivery Variance",
        "⏰ Delay Tracking",
        "🛠️ Product Analysis",
    ],
    label_visibility="collapsed"
)

captions = {
    "📈 Status Distribution": "Breakdown of orders by current status.",
    "🏭 Warehouse Performance": "Average delivery time per warehouse.",
    "🗺️ Regional Demand": "Total quantity ordered per region.",
    "📦 Delivery Variance": "Spread and distribution of delivery times across all orders.",
    "⏰ Delay Tracking": "Percentage of delayed orders per warehouse.",
    "🛠️ Product Analysis": "Order count, quantity, and average delivery time per product.",
}

st.subheader(view)
st.caption(captions[view])

chart_map = {
    "📈 Status Distribution": plot_status_distribution,
    "🏭 Warehouse Performance": plot_warehouse_performance,
    "🗺️ Regional Demand": plot_regional_demand,
    "📦 Delivery Variance": plot_delivery_variance,
    "⏰ Delay Tracking": plot_delay_tracking,
    "🛠️ Product Analysis": plot_product_analysis,
}

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.pyplot(chart_map[view](df))
st.markdown('</div>', unsafe_allow_html=True)