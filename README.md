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

## 🏗️ Fitur Utama
1. **🏠 Beranda**
   - Menyediakan pengenalan tentang dashboard dan navigasi.
   - Memberikan gambaran umum tentang isi dashboard.

2. **📅 Analisis Harian**
   - Menampilkan tabel data penyewaan sepeda per hari.
   - Memberikan informasi tren harian berdasarkan dataset.

3. **⏰ Analisis Jam**
   - Menampilkan tabel data penyewaan sepeda berdasarkan jam.
   - Memberikan wawasan mengenai pola penyewaan sepanjang hari.

4. **❓ Pertanyaan Analisis**
   - **Pengaruh kondisi cuaca terhadap penyewaan sepeda**
     - Menggunakan diagram boxplot untuk menunjukkan hubungan antara cuaca dan jumlah penyewaan sepeda.
     - Menjelaskan bagaimana kondisi cuaca (cerah, hujan, berkabut) memengaruhi jumlah penyewa.
   - **Pola penyewaan sepanjang hari**
     - Menggunakan diagram garis untuk menggambarkan tren penyewaan sepanjang hari.
     - Mengidentifikasi jam-jam puncak penyewaan sepeda.

## ✨ Kontribusi
Jika Anda ingin berkontribusi atau mengembangkan dashboard ini lebih lanjut, silakan fork repositori ini dan ajukan pull request.
