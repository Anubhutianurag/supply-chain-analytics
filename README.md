# 📦 Supply Chain Analytics Dashboard

A full-stack data analytics project that cleans, validates, analyzes, and visualizes supply chain order data through an interactive Streamlit dashboard.

**🔗 Live app:** [supply-chain-analytics.streamlit.app](https://supply-chain-analytics-ej42xzfqp9vux4fdmdkmww.streamlit.app/)

---
## Overview

This project takes a raw, messy supply chain orders dataset (155 records — duplicates, missing values, logically invalid dates, and an unreliable derived column) and turns it into a clean, validated, fully tested analytics pipeline with a styled, interactive dashboard.

## Tech Stack

- **Python** — pandas, numpy
- **Pydantic** — schema validation
- **Streamlit** — interactive web dashboard
- **Matplotlib / Seaborn** — data visualization
- **Pytest** — unit testing
- **Git / GitHub** — version control, feature-branch workflow with pull requests

## Project Structure

```
supply_chain_analytics/
├── app.py                      # Streamlit entry point
├── config/settings.py          # File paths & app configuration
├── models/order_schema.py      # Pydantic schema for order validation
├── processing/
│   ├── data_loader.py          # CSV loading
│   ├── data_cleaner.py         # Cleaning logic
│   └── analytics.py            # Aggregation & metrics functions
├── visualizations/              # 6 dashboard chart modules
├── tests/                      # Unit tests (pytest)
└── data/                       # Raw & cleaned datasets
```

## Running Locally

```bash
git clone https://github.com/Anubhutianurag/supply-chain-analytics.git
cd supply-chain-analytics
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Development Workflow

Built using a feature-branch Git workflow — each stage of the pipeline (cleaning, schema, analytics, dashboards, app, tests) was developed on its own branch, tested, and merged via pull request on `main`.

## Author

Built by [Anubhutianurag](https://github.com/Anubhutianurag)
