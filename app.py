import streamlit as st

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stTitle {
        color: #2E8B57;
        font-family: 'Arial', sans-serif;
    }
    .stCaption {
        color: #696969;
        font-size: 16px;
    }
    .stInfo {
        background-color: #e8f4fd;
        border-left: 5px solid #1e90ff;
        padding: 10px;
        border-radius: 5px;
    }
    .css-1d391kg {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #2E8B57;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #228B22;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Forecasting Harga Emas Antam",
    layout="wide"
)

st.title("Forecasting Harga Emas Antam")
st.caption("Aplikasi Streamlit untuk Hybrid SARIMAX, XGBoost, dan LightGBM")
st.info("Gunakan menu sidebar untuk membuka Menu Login, Home, Prediction, dan About")