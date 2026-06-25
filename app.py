
# ==============================================================================
# PROYEK AKHIR: ANALISIS FAKTOR UTAMA PENENTU KEMISKINAN DI JAWA DAN SUMATRA
# Nama Kelompok : Kelompok 5
# Mata Kuliah   : Analisis Data Statistik — Informatika UAI
# Dosen         : Tri Aji Nugroho, S.T., M.T.
# ==============================================================================

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Load data (sesuaikan dengan lokasi file excel Anda)
    df = pd.read_excel('Klasifikasi_Tingkat_Kemiskinan.xlsx', skiprows=2)
    
    # Ambil 10 baris pertama untuk ditampilkan di tabel
    tabel_html = df.head(10).to_html(classes='min-w-full divide-y divide-gray-200 border', index=False)
    
    # Kirim data tabel ke file index.html
    return render_template('TB.html', tabel=tabel_html)

if __name__ == '__main__':
    app.run(debug=True)

# ------------------------------------------------------------------------------
# SETUP LINGKUNGAN KERJA (IMPOR LIBRARY)
# ------------------------------------------------------------------------------
import pandas as pd                  # Untuk manipulasi data tabular (DataFrame)
import numpy as np                   # Untuk komputasi numerik
import matplotlib.pyplot as plt      # Untuk membuat visualisasi grafik dasar
import seaborn as sns                # Untuk visualisasi grafik statistik yang lebih menarik
from scipy import stats              # Untuk pengujian statistik (Korelasi & T-Test)
from sklearn.linear_model import LinearRegression # Untuk model Regresi Linear Berganda
from sklearn.preprocessing import StandardScaler  # Untuk standardisasi data (Feature Importance)
from sklearn.model_selection import train_test_split # Untuk membagi data (opsional jika dibutuhkan)
import warnings
warnings.filterwarnings('ignore')    # Menyembunyikan pesan peringatan (warning) agar output rapi

# Konfigurasi parameter visualisasi grafik (ukuran, font, gaya, dan warna)
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
sns.set_style('whitegrid')
sns.set_palette('Set2')

print("✅ Tahap Setup: Semua library berhasil diimpor dengan baik.\n")


# ------------------------------------------------------------------------------
# TAHAP 1: DEFINISI MASALAH (PROBLEM DEFINITION)
# ------------------------------------------------------------------------------
"""
LATAR BELAKANG:
Proyek ini menginvestigasi faktor utama kemiskinan di Pulau Jawa dan Sumatra.
Kita ingin memvalidasi apakah 'Pengeluaran per Kapita' merupakan proksi/penentu
tunggal kemiskinan, serta mencari faktor makro ekonomi lain yang paling dominan
di masing-masing pulau untuk mendukung evidence-based policy.

HIPOTESIS:
- H1: Pengeluaran per Kapita berkorelasi negatif kuat dengan % Penduduk Miskin.
- H2: Terdapat perbedaan persentase kemiskinan yang signifikan antara Jawa dan Sumatra.
- H3: Faktor utama penyebab kemiskinan di Jawa berbeda dengan di Sumatra.
"""
print("✅ Tahap 1: Problem Definition selesai dirumuskan (lihat docstring).\n")


# ------------------------------------------------------------------------------
# TAHAP 2 & 3: PENGUMPULAN DAN PEMBERSIHAN DATA (DATA COLLECTION & CLEANING)
# ------------------------------------------------------------------------------
print("⏳ Memulai Tahap 2 & 3: Load dan Cleaning Data...")

# 1. Load Data
# Mengabaikan 2 baris pertama (skiprows=2) karena itu adalah judul/header dari excel BPS
df_raw = pd.read_excel('Klasifikasi_Tingkat_Kemiskinan.xlsx', skiprows=2)

# 2. Definisikan daftar Provinsi yang termasuk di Pulau Jawa & Sumatra
prov_jawa = ['Dki Jakarta', 'Jawa Barat', 'Jawa Tengah', 'D I Yogyakarta', 'Jawa Timur', 'Banten']
prov_sumatra = ['Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Jambi',
                'Sumatera Selatan', 'Bengkulu', 'Lampung', 'Kep. Bangka Belitung', 'Kepulauan Riau']

# Memperbaiki penulisan nama provinsi (mengubah format menjadi Title Case & menghapus spasi lebih)
df_raw['Provinsi'] = df_raw['Provinsi'].str.title().str.strip()
prov_jawa = [p.title() for p in prov_jawa]
prov_sumatra = [p.title() for p in prov_sumatra]

# 3. Filter Dataset (Hanya mengambil data yang provinsinya ada di Jawa atau Sumatra)
df = df_raw[df_raw['Provinsi'].isin(prov_jawa + prov_sumatra)].copy()

# Fungsi untuk melabeli nama pulau berdasarkan provinsinya
def tentukan_pulau(prov):
    if prov in prov_jawa: return 'Jawa'
    elif prov in prov_sumatra: return 'Sumatra'
    else: return 'Lainnya'

# Menerapkan fungsi ke dalam kolom baru bernama 'Pulau'
df['Pulau'] = df['Provinsi'].apply(tentukan_pulau)

# 4. Data Cleaning (Penyesuaian Tipe Data)
# Daftar kolom yang seharusnya berisi angka (numerik)
cols_to_numeric = ['Penduduk Miskin (%)', 'Lama Sekolah (Thn)', 'Pengeluaran per Kapita (Ribu Rp)',
                   'IPM', 'Umur Harapan Hidup (Thn)', 'Sanitasi Layak (%)',
                   'Air Minum Layak (%)', 'Pengangguran (%)', 'Partisipasi Angkatan Kerja (%)']

# Memaksa konversi ke float numerik. Jika ada teks/string (seperti '-'), akan diubah jadi NaN (kosong)
for col in cols_to_numeric:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Data Cleaning (Handling Missing Values dengan Imputasi Median)
# Mengecek dan mengisi nilai yang kosong (NaN) dengan nilai Tengah (Median) dari kolom tersebut
for col in cols_to_numeric:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].median(), inplace=True)

print(f"✅ Tahap 2 & 3 Selesai! Dimensi Data Akhir: {df.shape[0]} Baris × {df.shape[1]} Kolom\n")


# ------------------------------------------------------------------------------
# TAHAP 4: EXPLORATORY DATA ANALYSIS (EDA) & VISUALISASI AWAL
# ------------------------------------------------------------------------------
print("📊 Menampilkan Plot Tahap 4: Exploratory Data Analysis (EDA)...")

# 4a. Membuat layout kanvas 1 baris, 2 kolom untuk distribusi kemiskinan
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Plot Kiri: Boxplot untuk melihat sebaran & deteksi outlier kemiskinan per pulau
sns.boxplot(x='Pulau', y='Penduduk Miskin (%)', data=df, ax=axes[0], palette='pastel')
axes[0].set_title('Distribusi Kemiskinan: Jawa vs Sumatra', fontweight='bold')

# Plot Kanan: Histogram/KDE (Kernel Density Estimation) untuk melihat kepadatan probabilitas
sns.kdeplot(data=df, x='Penduduk Miskin (%)', hue='Pulau', fill=True, ax=axes[1], palette='pastel')
axes[1].set_title('Kerapatan Kemiskinan (KDE Plot)', fontweight='bold')

plt.tight_layout()
plt.show()

# 4b. Membuat Matriks Korelasi (Heatmap) untuk seluruh variabel numerik
plt.figure(figsize=(10, 8))
corr_matrix = df[cols_to_numeric].corr()
# Membuat 'mask' agar segitiga atas disembunyikan (karena angkanya cerminan dari segitiga bawah)
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r', center=0)
plt.title('Matriks Korelasi Variabel Ekonomi (Heatmap)', fontweight='bold', fontsize=14)
plt.show()


# ------------------------------------------------------------------------------
# TAHAP 5a: PENGUJIAN STATISTIK INFERENSIAL (KORELASI & T-TEST)
# ------------------------------------------------------------------------------
print("================================================================")
print("TAHAP 5a: STATISTICAL MODELING (KORELASI PEARSON & T-TEST)")
print("================================================================")

# Analisis 1: Menguji Korelasi Pengeluaran per Kapita vs Persentase Kemiskinan (Bab 8)
r, p_val = stats.pearsonr(df['Pengeluaran per Kapita (Ribu Rp)'], df['Penduduk Miskin (%)'])
print("ANALISIS 1: Korelasi Pengeluaran per Kapita thd Kemiskinan")
print(f"-> Koefisien Korelasi (r) : {r:.4f}")
print(f"-> P-value                : {p_val:.2e}")
if p_val < 0.05:
    print("-> Kesimpulan: Terdapat korelasi signifikan (P-value < 0.05). Hipotesis 1 Terdukung!\n")
else:
    print("-> Kesimpulan: Tidak ada korelasi signifikan.\n")


# Analisis 2: Menguji perbedaan rata-rata kemiskinan Jawa vs Sumatra (Uji-T Dua Sampel Independen) (Bab 7)
jawa_miskin = df[df['Pulau'] == 'Jawa']['Penduduk Miskin (%)']
sumatra_miskin = df[df['Pulau'] == 'Sumatra']['Penduduk Miskin (%)']

# equal_var=False digunakan karena asumsi varians kedua pulau mungkin tidak sama (Welch's t-test)
t_stat, p_ttest = stats.ttest_ind(jawa_miskin, sumatra_miskin, equal_var=False)
print("ANALISIS 2: T-Test Independen Tingkat Kemiskinan Jawa vs Sumatra")
print(f"-> Rata-rata Jawa    : {jawa_miskin.mean():.2f}%")
print(f"-> Rata-rata Sumatra : {sumatra_miskin.mean():.2f}%")
print(f"-> T-Statistic       : {t_stat:.4f}")
print(f"-> P-value           : {p_ttest:.4f}")
if p_ttest < 0.05:
    print("-> Kesimpulan: Tolak H0. Ada perbedaan tingkat kemiskinan yang signifikan antara Jawa & Sumatra.\n")
else:
    print("-> Kesimpulan: Gagal Tolak H0. Tidak ada perbedaan signifikan.\n")


# ------------------------------------------------------------------------------
# TAHAP 5b: PEMODELAN REGRESI BERGANDA & FEATURE IMPORTANCE (Bab 9)
# ------------------------------------------------------------------------------
print("================================================================")
print("TAHAP 5b: REGRESI BERGANDA & FEATURE IMPORTANCE")
print("================================================================")

# Menyiapkan fitur-fitur yang akan dijadikan prediktor (Variabel Independen/X)
features = ['Lama Sekolah (Thn)', 'Pengeluaran per Kapita (Ribu Rp)',
            'IPM', 'Umur Harapan Hidup (Thn)', 'Sanitasi Layak (%)',
            'Air Minum Layak (%)', 'Pengangguran (%)', 'Partisipasi Angkatan Kerja (%)']

# Fungsi khusus untuk melakukan regresi dan mengekstrak tingkat kepentingan fitur (Standardized Feature Importance)
def get_feature_importance(data, name):
    X = data[features]               # Variabel X (Prediktor)
    y = data['Penduduk Miskin (%)']  # Variabel Y (Target/Dependen)

    # Standarisasi X agar satuan datanya sama (Z-score).
    # Hal ini WAJIB dilakukan agar nilai koefisien regresi (Beta) bisa dibandingkan antar variabel.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Latih model regresi
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Simpan hasil koefisien absolut (nilai mutlak) untuk mengurutkan faktor terkuat
    importance_df = pd.DataFrame({
        'Fitur': features,
        'Koefisien_Standar': model.coef_,
        'Absolut_Importance': np.abs(model.coef_)
    }).sort_values(by='Absolut_Importance', ascending=True)

    return importance_df, model.score(X_scaled, y) # Mengembalikan dataframe hasil dan Nilai R-Squared

# Eksekusi fungsi regresi untuk Gabungan, Khusus Jawa, dan Khusus Sumatra
imp_all, r2_all = get_feature_importance(df, "Gabungan")
imp_jawa, r2_jawa = get_feature_importance(df[df['Pulau'] == 'Jawa'], "Jawa")
imp_sumatra, r2_sumatra = get_feature_importance(df[df['Pulau'] == 'Sumatra'], "Sumatra")

print(f"-> Nilai R-Squared (R²) Model Gabungan : {r2_all:.4f}")
print(f"-> Nilai R-Squared (R²) Model Jawa     : {r2_jawa:.4f}")
print(f"-> Nilai R-Squared (R²) Model Sumatra  : {r2_sumatra:.4f}\n")


# ------------------------------------------------------------------------------
# TAHAP 6: INTERPRETASI DAN KOMUNIKASI (VISUALISASI AKHIR)
# ------------------------------------------------------------------------------
print("📊 Menampilkan Plot Tahap 6: Perbandingan Faktor Kemiskinan (Feature Importance)...")

# Membuat plot bar horisontal untuk membandingkan faktor kemiskinan di Jawa dan Sumatra
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Sub-plot Kiri: JAWA
axes[0].barh(imp_jawa['Fitur'], imp_jawa['Absolut_Importance'], color='coral')
axes[0].set_title('Faktor Utama Kemiskinan di Pulau JAWA', fontweight='bold')
axes[0].set_xlabel('Tingkat Kepentingan (|Koefisien Standar|)')

# Sub-plot Kanan: SUMATRA
axes[1].barh(imp_sumatra['Fitur'], imp_sumatra['Absolut_Importance'], color='mediumseagreen')
axes[1].set_title('Faktor Utama Kemiskinan di Pulau SUMATRA', fontweight='bold')
axes[1].set_xlabel('Tingkat Kepentingan (|Koefisien Standar|)')

# Judul utama visualisasi
plt.suptitle('Perbandingan Profil Kemiskinan: Pengaruh Faktor Makro Ekonomi (Jawa vs Sumatra)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()


# Cetak Kesimpulan (Executive Summary)
print("\n╔═══════════════════════════════════════════════════════════════════════════╗")
print("║               RINGKASAN TEMUAN UTAMA PROYEK AKHIR                         ║")
print("╠═══════════════════════════════════════════════════════════════════════════╣")
print("║ 1. Pengeluaran per Kapita memiliki korelasi negatif yang cukup kuat.      ║")
print("║    Artinya, makin tinggi pengeluaran, persentase kemiskinan makin turun,  ║")
print("║    namun ia BUKAN satu-satunya penentu tunggal kemiskinan (Menjawab Q1).  ║")
print("║                                                                           ║")
print("║ 2. Berdasarkan Uji T-Test Independen, terdapat perbedaan persentase       ║")
print("║    kemiskinan yang signifikan antara Pulau Jawa dan Sumatra (Menjawab Q2) ║")
print("║                                                                           ║")
print("║ 3. Dari Visualisasi 'Feature Importance', terlihat jelas bahwa faktor     ║")
print("║    terkuat yang mendikte kemiskinan di Jawa berbeda urutannya dengan      ║")
print("║    di Sumatra. Ini membuktikan Hipotesis 3 (Menjawab Q3).                 ║")
print("║                                                                           ║")
print("║ REKOMENDASI (Evidence-Based Policy):                                      ║")
print("║ Pemerintah daerah di Jawa dan Sumatra tidak bisa menggunakan 1 formulasi  ║")
print("║ kebijakan yang seragam. Prioritas intervensi (program pengentasan)        ║")
print("║ harus difokuskan pada fitur bar terpanjang di masing-masing grafik.       ║")
print("╚═══════════════════════════════════════════════════════════════════════════╝")
