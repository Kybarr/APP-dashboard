import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

img = Image.open('Dashboard/sepeda-gunung.jpg')
st.sidebar.image(img)

# Load dataset
day_df = pd.read_csv("Dashboard/day.csv")
hour_df = pd.read_csv("Dashboard/hour.csv")

# Sidebar Navigasi
st.sidebar.title("🚴‍♂️ Navigasi Dashboard")
halaman = st.sidebar.radio("🔍 Pilih Halaman:",
    ["🏠 Beranda", "📅 Analisis Harian", "⏰ Analisis Jam", "❓ Pertanyaan Analisis"])

# Beranda dengan Tampilan Lebih Menarik
st.title("📊 Dashboard Penyewaan Sepeda")
st.markdown("""
    🚲 **Selamat datang di Dashboard Penyewaan Sepeda!** 🚲
    
    Dashboard ini menyediakan berbagai analisis berdasarkan data penyewaan sepeda.
    - **Analisis Harian:** Melihat tren penyewaan harian.
    - **Analisis Jam:** Menganalisis pola penyewaan berdasarkan jam.
    - **Pertanyaan Analisis:** Menjawab pertanyaan penting terkait pola penyewaan.
    
    **Pilih menu di navigasi sidebar untuk melihat lebih banyak informasi!** 🚴‍♂️
""")

# Menampilkan Statistik Utama
total_penyewa = day_df["cnt"].sum()
col1, col2, col3 = st.columns(3)
col1.metric("📦 Total Penyewa", f"{total_penyewa:,}")

if halaman == "📅 Analisis Harian":
    st.subheader("📅 Analisis Penyewaan Sepeda Harian")
    st.markdown("""
    Berikut adalah data penyewaan sepeda per hari.
    Data ini mencakup jumlah sepeda yang disewa dalam berbagai kondisi cuaca dan faktor lainnya.
    """)
    st.dataframe(day_df)

elif halaman == "⏰ Analisis Jam":
    st.subheader("⏰ Distribusi Penyewaan Sepeda Per Jam")
    st.markdown("""
    Berikut adalah data penyewaan sepeda berdasarkan jam dalam sehari.
    Data ini membantu memahami kapan puncak penyewaan terjadi.
    """)
    st.dataframe(hour_df)   

elif halaman == "❓ Pertanyaan Analisis":
    st.subheader("❓ Analisis Berdasarkan Pertanyaan")
    
    st.markdown("### 1️⃣ Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?")
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='weathersit', y='cnt', data=day_df, palette='coolwarm')
    plt.title("Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda", fontsize=14)
    plt.xlabel("Kondisi Cuaca (1=Clear, 2=Cloudy, 3=Light Rain/Snow, 4=Heavy Rain/Snow)")
    plt.ylabel("Jumlah Penyewaan Sepeda")
    st.pyplot(plt)
    st.markdown("""
    Diagram berikut menunjukkan bagaimana kondisi cuaca mempengaruhi jumlah penyewaan sepeda.
    
    - **Kondisi 1**: Cerah/Berawan sedikit
    - **Kondisi 2**: Kabut + Berawan
    - **Kondisi 3**: Hujan ringan/Snow ringan
    - **Kondisi 4**: Hujan deras/Snow deras
    """)
    
    st.markdown("### 2️⃣ Bagaimana pola penyewaan sepeda berubah sepanjang hari, dan pada jam berapa penyewaan mencapai puncaknya?")
    hourly_avg_rentals = hour_df.groupby('hr')['cnt'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='hr', y='cnt', data=hourly_avg_rentals, marker='o', color='b')
    plt.title("Pola Penyewaan Sepeda Sepanjang Hari", fontsize=14)
    plt.xlabel("Jam dalam Sehari", fontsize=12)
    plt.ylabel("Rata-rata Jumlah Penyewaan", fontsize=12)
    plt.xticks(range(0, 24))
    plt.grid(True)
    st.pyplot(plt)
    st.markdown("""
    Diagram berikut menunjukkan pola rata-rata penyewaan sepeda sepanjang hari.
    
    - Penyewaan sepeda cenderung meningkat pada jam sibuk (pagi dan sore hari).
    - Menurun pada tengah malam hingga pagi dini hari.
    """)
    
    st.subheader("Clustering Result")
    st.dataframe(customer_category_counts)

st.sidebar.markdown("Data Diri :")
st.sidebar.info("Rizky Akbar")
st.sidebar.info("MC-54")
st.sidebar.info("MC006D5Y1259")

st.sidebar.markdown("""\n
    👇 **Dataset bisa didownload dibawah ini ya kakak** 👇
""")

@st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    )
    return df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.sidebar.download_button(
    label="Download Day.CSV",
    data=csv,
    file_name="day.csv",
    mime="text/csv",
    icon=":material/download:",
)

st.sidebar.download_button(
    label="Download hour.CSV",
    data=csv,
    file_name="hour.csv",
    mime="text/csv",
    icon=":material/download:",
)
