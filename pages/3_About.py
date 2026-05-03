import streamlit as st
from PIL import Image

# auth check
if "user_id" not in st.session_state:
    st.warning("silakan login terlebih dahulu")
    st.stop()

st.title("About")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.image("image/untar png.png", width=150)

st.write("""
aplikasi ini dikembangkan untuk mendukung forecasting harga emas Antam
menggunakan pendekatan:
- SARIMAX
- Hybrid SARIMAX-XGBoost
- Hybrid SARIMAX-LightGBM
""")

st.subheader("Tech Stack")
st.markdown("""
- Python
- Streamlit
- SQLite
- Statsmodels
- XGBoost
- LightGBM
""")

#st.subheader("Pengembang")
#st.write("Isi dengan nama, NIM, kk nya")