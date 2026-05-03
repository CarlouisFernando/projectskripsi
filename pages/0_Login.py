import streamlit as st
from utils.auth import register_user, login_user, ensure_admin_user
import sqlite3
from utils.db import init_auth_tables

st.title("Login Page")

conn = sqlite3.connect("data/app.db")
init_auth_tables(conn)
conn.close()

# admin user setup
ensure_admin_user()

if "user_id" in st.session_state:
    st.info(f"Anda sudah login sebagai {st.session_state.get('username')}.")
    if st.button("Kembali ke Home"):
        st.switch_page("pages/1_Home.py")
    st.stop()

menu = st.radio("Menu", ["Login", "Register"])

if menu == "Register":
    st.subheader("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if register_user(username, password):
            st.success("Register berhasil!")
        else:
            st.error("Username sudah ada!")

elif menu == "Login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user_id = login_user(username, password)

        if user_id:
            st.session_state.user_id = user_id
            st.session_state.username = username
            st.success("Login berhasil!")
            st.switch_page("pages/2_Prediction.py")
        else:
            st.error("Login gagal!")