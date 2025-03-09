# APP dashboard
 
 README - Dashboard Penyewaan Sepeda

 📌 Pendahuluan
Dashboard ini dikembangkan menggunakan Streamlit untuk menganalisis data penyewaan sepeda. Dashboard ini menampilkan informasi penting mengenai tren penyewaan sepeda berdasarkan berbagai faktor seperti waktu dan cuaca.

 📂 Persiapan
Sebelum menjalankan dashboard, pastikan Anda telah menginstal semua dependensi yang diperlukan. Instal dengan perintah berikut:

pip install streamlit pandas numpy pillow plotly

Selain itu, pastikan dataset berikut tersedia dalam direktori `Dashboard/`:
- `day.csv`  = Data penyewaan sepeda per hari
- `hour.csv` = Data penyewaan sepeda per jam
- `sepeda-gunung.jpg` → Gambar yang ditampilkan di sidebar
agar tidak terjadi error  saat dijalankan di streamlit
jika ingin dijalankan di lokal vscode maka tidak perlu menggunakan 'Dashboard/'

🚀 Cara Menjalankan Dashboard
1. Pastikan Anda berada di direktori tempat file skrip Streamlit disimpan.
2. Jalankan perintah berikut di vscode anda:
   
   python -m streamlit run Dashboard.py
  
3. Dashboard akan terbuka di browser lokal anda.

📖 Navigasi Dashboard
Dashboard memiliki beberapa halaman utama yang dapat diakses melalui sidebar:

1. 🏠 Beranda  
   Menampilkan ringkasan dan total penyewa sepeda.

2. 📅 Analisis Harian  
   Menampilkan tren penyewaan sepeda berdasarkan data harian dalam bentuk grafik garis.

3. ⏰ Analisis Jam  
   Menampilkan distribusi penyewaan sepeda berdasarkan jam dalam bentuk boxplot.

4. ☁️ Statistik Cuaca  
   Menunjukkan pengaruh cuaca terhadap jumlah penyewaan sepeda.

5. 📊 Analisis Lanjutan 
   Menganalisis data menggunakan metode RFM Analysis dan Clustering menampilkan segmentasi pelanggan berdasarkan jumlah penyewaan.

 🎯 Fitur Utama
- Filter Data Berdasarkan Tanggal: Memilih rentang tanggal untuk menyesuaikan analisis.
- isualisasi Data: Menggunakan berbagai grafik interaktif untuk menyajikan informasi.
- *Analisis Statistik: Melakukan analisis terhadap tren penyewaan dan pengaruh cuaca.
- Download Dataset: Pengguna dapat mengunduh file `day.csv` dan `hour.csv` langsung dari sidebar.

 🔍 Informasi Tambahan
RFM Analysis pada halaman *Analisis Lanjutan* membagi pelanggan ke dalam kategori berdasarkan jumlah penyewaan:
- Low Usage (<500 penyewaan)
- Regular User (500-1500 penyewaan)
- High Usage (>1500 penyewaan)
