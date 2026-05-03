import streamlit as st
from utils.auth import get_all_users, delete_user

# auth check
if "user_id" not in st.session_state:
    st.warning("silakan login terlebih dahulu")
    st.stop()

if st.session_state.get("username") != "admin":
    st.error("Akses admin hanya untuk user 'admin'.")
    st.info("Login dengan akun admin untuk mengelola pengguna.")
    st.stop()

st.title("Admin Panel")
st.subheader("Kelola Akun Pengguna")

st.info(
    "Halaman ini hanya tersedia untuk akun admin. "
    "Gunakan untuk melihat dan menghapus akun terdaftar."
)

users = get_all_users()
if not users:
    st.info("Belum ada akun pengguna terdaftar.")
else:
    user_table = [
        {"id": row[0], "username": row[1], "created_at": row[2]}
        for row in users
    ]
    st.dataframe(user_table, use_container_width=True)

    usernames = [row["username"] for row in user_table]
    selected_user = st.selectbox("Pilih username untuk dihapus", usernames)

    if st.button("Hapus akun pengguna", use_container_width=True):
        if selected_user == "admin":
            st.warning("Akun admin tidak dapat dihapus dari halaman ini.")
        else:
            if delete_user(selected_user):
                st.success(f"Akun '{selected_user}' berhasil dihapus.")
                st.rerun()
            else:
                st.error(f"Gagal menghapus akun '{selected_user}'.")
