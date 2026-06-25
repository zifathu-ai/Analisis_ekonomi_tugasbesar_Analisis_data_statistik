# Analisis_ekonomi_tugasbesar_Analisis_data_statistik

# DOKUMEN UTAMA PERENCANAAN PROYEK AKHIR

Kelompok 5 | Analisis Data Statistik | Informatika — UAI 
Dosen Pengampu: Tri Aji Nugroho, S.T., M.T. 
Topik Utama: Analisis Faktor Utama Penentu Kemiskinan di Pulau Jawa dan Sumatra

Disusun Oleh:
- Zhillal Fathurahman - 0102525020
- Muhammad Raafi Putra Arya - 0102525009
- Panca Pamungkas - 0102525013
- Raya Aulia Abdilah - 0102525016


# Bagian 1: Ringkasan Konsep Utama
Proyek ini mengusung konsep Feature Importance & Regional Profiling berbasis data (data-driven) untuk membongkar dan memetakan variabel ekonomi mana yang paling krusial dalam mendikte tingkat kemiskinan di Pulau Jawa dan Sumatra: 
•	Tingkat 1 — Evaluasi Daya Beli (Mikro): Menguji seberapa kuat dan akurat variabel Pengeluaran per Kapita dapat diandalkan sebagai instrumen tunggal atau tolak ukur dalam merefleksikan tingkat kemiskinan masyarakat di tingkat regional.
•	Tingkat 2 — Identifikasi Faktor Utama (Makro): Menggunakan pemodelan statistik kuantitatif untuk memeras seluruh variabel ekonomi dan ketenagakerjaan yang ada, guna menemukan "faktor utama" (prediktor paling dominan) pemicu kemiskinan di masing-masing pulau.

Tujuan akhirnya adalah memindahkan paradigma kebijakan penanganan kemiskinan dari yang sifatnya generalisasi atau "kira-kira" menjadi berbasis bukti data yang sangat spesifik (evidence-based policy) sesuai karakteristik unik Pulau Jawa vs Pulau Sumatra. 

# Bagian 2: Komponen Problem Definition (Definisi Masalah) 

## 2.1 Latar Belakang & Konteks (Background) 
Pulau Jawa dan Sumatra merupakan dua kontributor terbesar bagi PDB nasional. Namun, kantong-kantong kemiskinan di kedua wilayah ini memiliki karakteristik ekonomi yang berbeda. Sering kali terjadi paradoks ekonomi, misalnya suatu daerah memiliki produktivitas ekonomi (PDRB) yang sangat masif namun angka kemiskinannya tetap tinggi karena masalah distribusi pendapatan atau penyerapan tenaga kerja (Pengangguran dan TPAK). Oleh karena itu, diperlukan analisis statistik yang terarah untuk mengidentifikasi apa sebenarnya faktor utama yang menjadi motor penggerak kemiskinan di kedua wilayah tersebut agar alokasi program intervensi pemerintah menjadi lebih efisien dan tepat sasaran. 

## 2.2	Pertanyaan Penelitian (Research Questions) 
•	Q1 (Pembuktian Khusus): Apakah Pengeluaran per Kapita terbukti secara signifikan menjadi penentu utama  tingkat kemiskinan di Pulau Jawa dan Sumatra?
•	Q2 (Eksplorasi Faktor Dominan): Faktor ekonomi manakah yang menjadi penentu utama (paling dominan) dalam memengaruhi tingkat kemiskinan di masing-masing wilayah (Jawa vs Sumatra)?

## 2.3 Formulasi Hipotesis Formal (Statistical Hypothesis)
Untuk menjawab Q1, digunakan uji signifikansi parsial pada model regresi linear berganda:
•	Hipotesis Nol (H0): Pengeluaran per Kapita tidak memiliki pengaruh signifikan terhadap persentase Penduduk Miskin di Pulau Jawa dan Sumatra.
•	Hipotesis Alternatif (H1): Pengeluaran per Kapita memiliki pengaruh signifikan terhadap persentase Penduduk Miskin di Pulau Jawa dan Sumatra.

## 2.4 Identifikasi Variabel (Variable Identification) 
•	Variabel Terikat / Dependen (Y): Penduduk Miskin (%) dan status Klasifikasi daerah. 
•	Variabel Bebas / Independen (X): Pengeluaran per Kapita (Ribu Rp), Pengangguran (%), Partisipasi Angkatan Kerja (%), dan PDRB (Rp). 

## 2.5 Penentuan Metode Statistik & Visualisasi (Metode yang Tepat)
Untuk kasus yang ingin lo buktikan, metode terbaik dibagi menjadi dua tahapan ini:
-	Bab 02 (Statistika Deskriptif): Digunakan untuk meringkas data (mean, median, standar deviasi) dan profil awal kemiskinan di Jawa dan Sumatra.

-	Bab 03 (Visualisasi Data): Digunakan untuk membuat Boxplot dan KDE Plot (untuk melihat sebaran data) serta Bar Chart (untuk membandingkan faktor utama).

-	Bab 07 (Uji Hipotesis): Digunakan untuk melakukan Uji t (T-Test) untuk membandingkan rata-rata tingkat kemiskinan antara Jawa dan Sumatra.

-	Bab 08 (Korelasi & Regresi Linear): Digunakan untuk melakukan Uji Korelasi Pearson antara Pengeluaran per Kapita dengan persentase penduduk miskin.

-	Bab 09 (Regresi Berganda): Digunakan untuk model Regresi Linear Berganda, termasuk Uji F (untuk kelayakan model secara simultan) dan penggunaan Koefisien Beta untuk menentukan Feature Importance.
  
## 2.6 Batasan Masalah 
Analisis dibatasi hanya menggunakan data sekunder dari BPS yang mencakup wilayah Pulau Jawa (119 Kabupaten/Kota) dan Pulau Sumatra (154 Kabupaten/Kota) dengan total 273 observasi. Faktor utama penentu kemiskinan dibatasi pada indikator ekonomi riil yang tersedia di dalam dataset, tidak menganalisis kebijakan upah regional (UMK) atau bantuan sosial spesifik. 
Bagian 3: Dampak Nyata Hasil Analisis (Acuan Kebijakan) 
•	Akurasi Diagnosis Ekonomi Regional: Memberikan arah kebijakan yang spesifik bagi pemerintah daerah. Membantu pemerintah memprioritaskan pembangunan. 
•	Efisiensi Anggaran Fiskal: Membantu Bappeda menghindari pemborosan anggaran akibat menyamaratakan program penanggulangan kemiskinan di setiap pulau. 

# Bagian 3: Checklist Persyaratan Kelayakan Topik (SMART-D) 

## Kriteria	Penjelasan Kriteria	Bukti Pemenuhan Kelompok 5	Status
1. Specific	Fokus pada satu fenomena yang jelas 	Fokus mengupas faktor penentu utama kemiskinan (daya beli vs ketenagakerjaan) secara komparatif di Jawa dan Sumatra.	✓ Terpenuhi
   
2. Measurable	Variabel dapat diukur secara kuantitatif 	Menggunakan variabel numerik ekonomi: Persentase (%), Nilai Rupiah, dan Ribu Rupiah.	✓ Terpenuhi
    
3. Achievable	Data tersedia dan dapat diakses 	Data bersumber riil dari BPS (Klasifikasi_Tingkat_Kemiskinan.xlsx) dengan total gabungan 273 baris data (lolos syarat minimal 200).	✓ Terpenuhi

4. Relevant	Bermakna bagi pemangku kepentingan 	Hasilnya memberikan rekomendasi berbasis data kepada pemerintah daerah mengenai prioritas program pengentasan kemiskinan.	✓ Terpenuhi

5. Time-bound	Periode data jelas dan terdefinisi 	Menggunakan satu periode data tahun berjalan (cross-section) regional yang terstandardisasi oleh BPS.	✓ Terpenuhi

6. Data-driven	Didukung penuh data kuantitatif 	Penentuan faktor utama sepenuhnya didasarkan pada hasil angka nilai koefisien regresi statistik dan p-value terkecil.	✓ Terpenuhi

# Bagian 4 : Checklist Persyaratan Umum Tugas Akhir 
•	✓ Batas Minimal Baris Data: Menggabungkan Jawa dan Sumatra menghasilkan 273 baris data riil, memenuhi kualifikasi tugas (minimal 200 observasi). 
•	✓ Variasi Metode Statistik: Menerapkan dua rumpun metode berbeda (Bab 3: Statistika Deskriptif, Korelasi, & Visual EDA, serta Bab 8: Inferensial Regresi Linear Berganda). 
•	✓ Komponen Transparansi Akademik (AI Usage Log): Dokumentasi penggunaan AI dalam pemilahan wilayah (Jawa-Sumatra) dan rekonstruksi hipotesis regresi telah dicatat sejak awal. 
•	✓ Kesiapan Tahap Komunikasi: Hasil pemodelan dirancang untuk menghasilkan visualisasi kontribusi faktor (feature importance) yang sangat aplikatif dan menarik saat dipresentasikan di hadapan Pak Tri Aji. 

STATUS AKHIR DOKUMEN
LENGKAP, VALID, & SIAP EKSEKUSI 

