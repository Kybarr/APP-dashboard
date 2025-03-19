import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



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

    Dashboard keren
""")

# Menampilkan Statistik Utama
total_penyewa = day_df["cnt"].sum()
col1, col2, col3 = st.columns(3)
col1.metric("📦 Total Penyewa", f"{total_penyewa:,}")

if halaman == "📅 Analisis Harian":
    st.subheader("📅 Analisis Penyewaan Sepeda Harian")

    # Pastikan kolom tanggal dalam format datetime
    day_df["dteday"] = pd.to_datetime(day_df["dteday"])

    # Menambahkan Filter Tanggal dengan Date Input
    col1, col2 = st.columns(2)
    min_date = day_df["dteday"].min().date()
    max_date = day_df["dteday"].max().date()

    with col1:
        start_date = st.date_input("Pilih Tanggal Mulai", min_value=min_date, max_value=max_date, value=min_date)
    with col2:
        end_date = st.date_input("Pilih Tanggal Akhir", min_value=min_date, max_value=max_date, value=max_date)

    # Menambahkan Filter Musim
    season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    day_df["season_label"] = day_df["season"].map(season_mapping)

    selected_season = st.selectbox("Pilih Musim:", ["Semua"] + list(season_mapping.values()))

    # Filter dataset berdasarkan pilihan pengguna
    filtered_df = day_df[
        (day_df["dteday"].dt.date >= start_date) & 
        (day_df["dteday"].dt.date <= end_date)
    ]

    if selected_season != "Semua":
        filtered_df = filtered_df[filtered_df["season_label"] == selected_season]

    # Menampilkan Data yang Telah Difilter
    st.dataframe(filtered_df)

    # Visualisasi Penyewaan Sepeda dengan Plotly
    st.markdown("### 📈 Tren Penyewaan Sepeda Berdasarkan Filter")
    fig = px.line(filtered_df, x="dteday", y="cnt", color="season_label",
                  labels={"cnt": "Jumlah Penyewaan", "dteday": "Tanggal"},
                  title="Tren Penyewaan Sepeda Berdasarkan Musim & Tanggal")

    st.plotly_chart(fig, use_container_width=True)


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
