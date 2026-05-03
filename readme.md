# Forecasting Harga Emas Antam

Aplikasi Streamlit untuk memprediksi harga emas Antam menggunakan kombinasi model statistik dan machine learning.

---

## 📁 Struktur Folder dan File

### 📂 Root Directory

| File | Deskripsi |
|------|-----------|
| `app.py` | File utama aplikasi Streamlit. Menjalankan server dan mengatur konfigurasi halaman. |
| `requirements.txt` | Daftar paket Python yang diperlukan (streamlit, pandas, scikit-learn, dll). |
| `readme.md` | Dokumentasi proyek ini. |
| `debug_chart_logam_mulia.html` | File HTML untuk debugging visualisasi chart (development). |
| `forecasting.db` | Database SQLite yang dibuat otomatis saat aplikasi berjalan. |

---

### 📂 `data/` — Data Input

Folder ini menyimpan data historis dan referensi yang digunakan untuk training dan forecasting.

| File | Deskripsi |
|------|-----------|
| `harga_emas_antm.csv` | Data historis harga emas Antam (tanggal, harga beli, harga jual). |
| `Data Historis XAU_USD.csv` | Data kurs XAU/USD (Gold vs USD) sebagai variabel eksogen. |
| `data kurs usd idr.xlsx` | Data kurs USD/IDR historis. |
| `BI-7Day-RR.xlsx` | Data suku bunga BI-7DRR (variabel eksogen). |
| `Data Inflasi.xlsx` | Data inflasi tahunan (YoY) Indonesia. |
| `master_static.csv` | Gabungan data statis (XAU/USD, USD/IDR, inflasi, BI-7DRR) untuk modeling. |
| `forecasting.db` | Salinan database SQLite untuk backup. |

---

### 📂 `models/` — Model Terlatih

Folder ini menyimpan model yang sudah dilatih dan konfigurasi.

| File | Deskripsi |
|------|-----------|
| `config.json` | Konfigurasi model: horizon, fitur, parameter model. |
| `sarimax_fit.pkl` | Model SARIMAX yang sudah di-fit (untuk semua horizon). |
| `xgb_h1.pkl` s/d `xgb_h7.pkl` | Model XGBoost untuk horizon H+1 sampai H+7. |
| `lgb_h1.pkl` s/d `lgb_h7.pkl` | Model LightGBM untuk horizon H+1 sampai H+7. |
| `lgb_h1.txt` s/d `lgb_h7.txt` | File teks berisi feature importance model LightGBM. |
| `metrics_all_horizons.csv` | Tabel metrik evaluasi (RMSE, MAE, MAPE) semua model per horizon. |
| `best_model_per_horizon.csv` | Rekomendasi model terbaik untuk setiap horizon berdasarkan metrik. |

---

### 📂 `utils/` — Modul Pendukung

Folder ini berisi fungsi-fungsi utility yang digunakan di seluruh aplikasi.

| File | Fungsi |
|------|--------|
| `db.py` | Mengelola koneksi SQLite, membuat tabel, insert/update data. |
| `auth.py` | Menangani autentikasi: registrasi, login, verifikasi password, manajemen session. |
| `scraper.py` | Mengambil data terbaru dari sumber (Antam, USD/IDR) via web scraping. |
| `preprocessing.py` | Membersihkan dan transformasi data: fill missing, scaling, join dataset. |
| `model_loader.py` | Memuat model terlatih dari folder `models/`. |
| `predictor.py` | Menjalankan prediksi menggunakan model yang dipilih dan menyimpan riwayat. |
| `export_utils.py` | Mengekspor hasil prediksi ke format CSV atau Excel. |
| `static_data.py` | Mengatur dan memuat data statis seperti XAU/USD, USD/IDR, inflasi, dan BI-7DRR. |

---

### 📂 `pages/` — Halaman Streamlit

Folder ini berisi halaman-halaman aplikasi yang diakses via sidebar.

| File | Halaman | Deskripsi |
|------|---------|-----------|
| `0_Login.py` | **Login** | Halaman autentikasi: registrasi akun baru, login dengan username/password. |
| `1_Home.py` | **Home** | Halaman utama: deskripsi aplikasi, model yang digunakan, tabel metrik, grafik RMSE. |
| `2_Prediction.py` | **Prediction** | Halaman utama untuk menjalankan forecasting: inisialisasi data, pilih horizon, jalankan prediksi, lihat hasil, download. |
| `3_About.py` | **About** | Halaman info: tujuan proyek, stack teknologi, info pengembang. |

---

### 📂 `notebook/` — Development

| File | Deskripsi |
|------|-----------|
| `Client_Forecasting_Hybrid_Model.ipynb` | Jupyter Notebook untuk eksperimen model, EDA, dan evaluasi. |

---

## ⚙️ Setup Lingkungan

1. Buka terminal di folder proyek:

```powershell
cd "c:\Users\NAUFAL FAIZ\Documents\Client Forecasting Hybrid Antam"
```

2. Buat virtual environment:

```powershell
python -m venv .venv
```

3. Aktifkan environment:

- **PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

- **Command Prompt:**
```cmd
.venv\Scripts\activate.bat
```

4. Install dependensi:

```powershell
pip install -r requirements.txt
```

---

## 🚀 Menjalankan Aplikasi

Setelah environment aktif dan dependensi terpasang:

```powershell
streamlit run app.py
```

Buka browser ke `http://localhost:8501`.

---

## 🧭 Tutorial Penggunaan

Ikuti langkah berikut untuk menggunakan aplikasi:

### 🔐 1. Login / Register
1. Buka aplikasi
2. Untuk pengguna biasa: pilih menu **Register** untuk membuat akun baru
3. Login menggunakan username dan password yang terdaftar

💡 Untuk mengakses halaman admin, gunakan akun default:
- username: `admin`
- password: `admin`

> Halaman login akan menolak form baru jika Anda sudah login, sehingga tidak bisa login ulang dari halaman yang sama.

---

### 🔰 2. Setup Awal (Pertama Kali)
1. Masuk ke halaman **Prediction**
2. Klik **Initialize Historical Data**
3. Sistem akan mengambil:
   - Data harga emas Antam
   - Data kurs USD/IDR

📌 Langkah ini cukup dilakukan **sekali di awal**

---

### 📊 3. Upload Data Variabel Tambahan
Upload data berikut secara manual:

- XAU/USD
- Inflasi YoY
- BI Rate

Langkah:
1. Buka bagian **Update Data Static**
2. Upload masing-masing file
3. Klik tombol update sesuai variabel

📌 Dilakukan saat:
- pertama kali setup
- ada update data dari sumber resmi

---

### 🔄 4. Update Data Terbaru
Klik tombol **Update Data** untuk mengambil:
- harga emas Antam terbaru
- kurs USD/IDR terbaru

📌 Disarankan dilakukan **1x sehari**

---

### 🔮 5. Menjalankan Prediksi
1. Pilih horizon prediksi (H+1 s.d H+7)
2. Klik **Run Prediction**
3. Tunggu proses selesai

---

### 📈 6. Melihat Hasil
Aplikasi akan menampilkan:
- tabel prediksi
- grafik harga aktual
- grafik hasil forecasting
- perbandingan model
- feature importance

---

### 💾 7. Menyimpan Hasil
Download hasil prediksi melalui:

- **Download ZIP**

Isi file ZIP:
- `prediction.csv`
- `prediction.xlsx`
- `actual_plot.png`
- `forecast_plot.png`
- `feature_importance_xgb.png`
- `feature_importance_lgb.png`

---

### 🕘 8. Riwayat Prediksi
Setiap pengguna memiliki riwayat prediksi sendiri yang mencatat:
- waktu prediksi
- horizon
- rentang data yang digunakan

📌 Hanya metadata yang disimpan, bukan seluruh hasil prediksi
## 📌 Penjelasan Model

Aplikasi ini menggunakan pendekatan **hybrid** yang menggabungkan:

| Model | Tipe | Keterangan |
|-------|------|------------|
| **SARIMAX** | Statistik | Model time series dengan variabel eksogen. |
| **Hybrid SARIMAX-XGBoost** | Machine Learning | Residual SARIMAX diprediksi lanjut oleh XGBoost. |
| **Hybrid SARIMAX-LightGBM** | Machine Learning | Residual SARIMAX diprediksi lanjut oleh LightGBM. |

**Variabel eksogen yang digunakan:**
- XAU/USD (harga emas dunia)
- USD/IDR (kurs Rupiah)
- Inflasi YoY Indonesia
- BI-7DRR (suku bunga BI)

---

## 📝 Catatan Penting

- Pastikan file `models/config.json` dan model `.pkl` tersedia untuk melihat feature importance.
- Pastikan `data/master_static.csv` ada sebelum menjalankan prediksi.
- Jika data belum diinisialisasi, klik **Initialize Historical Data** pada halaman Prediction terlebih dahulu.
- Jika muncul error saat prediksi:
  - Pastikan semua data sudah tersedia (Antam, USD/IDR, XAU/USD, Inflasi, BI Rate)
- Data inflasi dan BI Rate bersifat bulanan → sistem akan menyesuaikan otomatis
- Model menggunakan kombinasi:
  - SARIMAX (baseline)
  - Hybrid SARIMAX + XGBoost
  - Hybrid SARIMAX + LightGBM

---

## 👤 Manajemen Akun

Aplikasi menggunakan sistem login sederhana berbasis database SQLite.

### 📂 Lokasi Database
Data akun dan riwayat prediksi disimpan pada file:

data/app.db

---

### 🔍 Melihat Akun yang Terdaftar

Untuk melihat daftar akun:

1. Gunakan aplikasi seperti **DB Browser for SQLite**
2. Buka file `data/app.db`
3. Pilih tab **Browse Data**
4. Pilih tabel **users**

Di tabel tersebut akan terlihat:
- id pengguna
- username
- waktu pembuatan akun

📌 Password tidak dapat dilihat karena disimpan dalam bentuk hash (keamanan)

---

### 🗑️ Menghapus Akun

Penghapusan akun kini bisa dilakukan dari antarmuka aplikasi melalui halaman `Admin` jika Anda login sebagai pengguna `admin`.

Aplikasi secara otomatis membuat akun admin default dengan kredensial:
- username: `admin`
- password: `admin`

Jika akun admin sudah ada, program tidak membuat duplikat.

Langkah alternatif (jika belum menggunakan halaman admin):

1. Buka file `data/app.db` menggunakan DB Browser
2. Pilih tabel `users`
3. Cari username yang ingin dihapus
4. Hapus baris tersebut lalu klik **Write Changes**

Alternatif menggunakan SQL:

DELETE FROM users WHERE username = 'nama_user';

---

### ⚠️ Catatan

- Halaman admin hanya dapat diakses oleh user `admin`
- Penghapusan akun hanya dapat dilakukan untuk akun non-admin
- Pengguna biasa tetap membuat akun lewat menu `Register` dan tidak dapat mengakses panel admin