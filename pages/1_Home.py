import streamlit as st
import pandas as pd
import plotly.express as px

# auth check
if "user_id" not in st.session_state:
    st.warning("silakan login terlebih dahulu")
    st.stop()

st.title("Home")
st.subheader("sistem Forecasting Harga Emas Antam")

st.write("""
aplikasi ini menggunakan tiga model:
1. SARIMAX
2. Hybrid SARIMAX-XGBoost
3. Hybrid SARIMAX-LightGBM
""")

st.markdown("**variabel eksogen yang digunakan:** XAU/USD, Kurs USD/IDR, Inflasi YoY, BI-7DRR Rate")

metrics_path = "models/metrics_all_horizons.csv"
best_path = "models/best_model_per_horizon.csv"

try:
    metrics_df = pd.read_csv(metrics_path)
    best_df = pd.read_csv(best_path)

    st.subheader("Highlight Model Terbaik")
    st.dataframe(best_df, use_container_width=True)

    st.subheader("Ringkasan Performa Model")
    st.dataframe(metrics_df, use_container_width=True)

    st.subheader("Visualisasi RMSE per Horizon")
    fig = px.bar(metrics_df, x="horizon", y="RMSE", color="model", barmode="group", title="RMSE untuk Setiap Model per Horizon")
    st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.warning("file metrik model belum tersedia di folder models")