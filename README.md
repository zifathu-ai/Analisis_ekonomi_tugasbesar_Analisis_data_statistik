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
Kemiskinan merupakan salah satu tantangan pembangunan yang paling mendasar di Indonesia. Meskipun secara nasional tingkat kemiskinan terus menurun, disparitas antardaerah tetap menjadi persoalan serius yang belum terselesaikan. Pulau Jawa dan Sumatra, sebagai dua kontributor terbesar bagi Produk Domestik Bruto (PDB) nasional, masih menyimpan kantong-kantong kemiskinan yang signifikan dengan karakteristik ekonomi yang berbeda satu sama lain (Mustika et al., 2023).


Tujuan akhirnya adalah memindahkan paradigma kebijakan penanganan kemiskinan dari yang sifatnya generalisasi atau "kira-kira" menjadi berbasis bukti data yang sangat spesifik (evidence-based policy) sesuai karakteristik unik Pulau Jawa vs Pulau Sumatra. 

# Bagian 2: Komponen Problem Definition (Definisi Masalah) 

## 2.1 Latar Belakang & Konteks (Background) 
Pulau Jawa dan Sumatra merupakan dua kontributor terbesar bagi PDB nasional. Namun, kantong-kantong kemiskinan di kedua wilayah ini memiliki karakteristik ekonomi yang berbeda. Sering kali terjadi paradoks ekonomi, misalnya suatu daerah memiliki produktivitas ekonomi (PDRB) yang sangat masif namun angka kemiskinannya tetap tinggi karena masalah distribusi pendapatan atau penyerapan tenaga kerja (Pengangguran dan TPAK). Oleh karena itu, diperlukan analisis statistik yang terarah untuk mengidentifikasi apa sebenarnya faktor utama yang menjadi motor penggerak kemiskinan di kedua wilayah tersebut agar alokasi program intervensi pemerintah menjadi lebih efisien dan tepat sasaran. 

## 2.2	Pertanyaan Penelitian (Research Questions) 


Q1 (Pembuktian Khusus): Apakah Pengeluaran per Kapita terbukti secara signifikan menjadi penentu utama tingkat kemiskinan di Pulau Jawa dan Sumatra?

Q2 (Eksplorasi Faktor Dominan): Faktor manakah yang menjadi penentu utama (paling dominan) dalam memengaruhi tingkat kemiskinan di masing-masing wilayah (Jawa dan Sumatra)?


## 2.3 Formulasi Hipotesis Formal (Statistical Hypothesis)
Untuk menjawab Q1, digunakan uji signifikansi parsial pada model regresi linear berganda:
•	Hipotesis Nol (H0): Pengeluaran per Kapita tidak memiliki pengaruh signifikan terhadap persentase Penduduk Miskin di Pulau Jawa dan Sumatra.
•	Hipotesis Alternatif (H1): Pengeluaran per Kapita memiliki pengaruh signifikan terhadap persentase Penduduk Miskin di Pulau Jawa dan Sumatra.

## 2.4 Identifikasi Variabel (Variable Identification) 
•	Variabel Terikat / Dependen (Y): Penduduk Miskin (%) dan status Klasifikasi daerah. 
•	Variabel Bebas / Independen (X): Pengeluaran per Kapita (Ribu Rp), Pengangguran (%), Partisipasi Angkatan Kerja (%), dan PDRB (Rp). 

## 2.5 Penentuan Metode Statistik & Visualisasi (Metode yang Tepat)
Untuk kasus yang ingin lo buktikan, metode terbaik dibagi menjadi dua tahapan ini:
Metode Statistika

Penelitian ini menggunakan tiga metode utama, yaitu Statistika Deskriptif, Korelasi Pearson, dan Regresi Linear Berganda OLS Terstandardisasi. Pemilihan metode ini didasarkan pada kebutuhan untuk memahami karakteristik data, menguji hubungan antar variabel, serta mengidentifikasi faktor dominan penentu kemiskinan di Pulau Jawa dan Sumatra.

1. Statistika Deskriptif  
Tujuan: Memberikan gambaran umum mengenai distribusi data tiap indikator, seperti rata-rata, median, standar deviasi, dan koefisien variasi.  
Alasan: Digunakan untuk memahami pola sebaran dan disparitas antar wilayah sebelum dilakukan analisis inferensial.  

2. Korelasi Pearson  
Tujuan: Mengukur kekuatan dan arah hubungan linear antara Pengeluaran per Kapita dengan Persentase Penduduk Miskin (%).  
Alasan: Dipilih untuk menjawab pertanyaan penelitian Q1, yaitu apakah daya beli masyarakat signifikan memengaruhi tingkat kemiskinan.  

3. Regresi Linear Berganda OLS Terstandardisasi  
Tujuan: Mengidentifikasi faktor dominan dari 8 variabel independen (pendidikan, daya beli, kesehatan, sanitasi, pengangguran, partisipasi kerja, PDRB, dll.) terhadap tingkat kemiskinan.  
Alasan: Digunakan untuk menjawab pertanyaan penelitian Q2, yaitu faktor mana yang paling berpengaruh terhadap kemiskinan di masing-masing wilayah. Standardisasi dilakukan agar koefisien regresi dapat dibandingkan secara adil antar variabel.  


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

