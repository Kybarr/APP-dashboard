import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

img = Image.open('sepeda-gunung.jpg')
st.sidebar.image(img)

# Load dataset
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Konversi kolom tanggal ke format datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

day_df["temp_C"] = day_df["temp"] * 41
day_df["atemp_C"] = day_df["atemp"] * 50
day_df["humidity_percent"] = day_df["hum"] * 100
day_df["windspeed_kmh"] = day_df["windspeed"] * 67

# Sidebar Navigasi
st.sidebar.title("🚴‍♂️ Navigasi Dashboard")
halaman = st.sidebar.radio("🔍 Pilih Halaman:",
    ["🏠 Beranda", "📅 Analisis Harian", "⏰ Analisis Jam", "☁️ Statistik Cuaca", "📊 Analisis Lanjutan"])

# Beranda dengan Tampilan Lebih Menarik
st.title("📊 Dashboard Penyewaan Sepeda")
st.markdown("""
    🚲 **Selamat datang di Dashboard Penyewaan Sepeda!** 🚲
    
    Dashboard ini menyediakan berbagai analisis berdasarkan data penyewaan sepeda.
    
    **Pilih menu di navigasi sidebar untuk melihat lebih banyak informasi!** 🚴‍♂️
""")

# Menampilkan Statistik Utama
total_penyewa = day_df["cnt"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("📦 Total Penyewa", f"{total_penyewa:,}")

# Filter Data berdasarkan Rentang Tanggal
st.sidebar.subheader("📆 Filter Data")
min_date, max_date = st.sidebar.date_input(
    "Pilih Rentang Tanggal", [day_df["dteday"].min(), day_df["dteday"].max()],
    min_value=day_df["dteday"].min(),
    max_value=day_df["dteday"].max()
)

day_df_filtered = day_df[(day_df["dteday"] >= pd.Timestamp(min_date)) & (day_df["dteday"] <= pd.Timestamp(max_date))]
hour_df_filtered = hour_df[(hour_df["dteday"] >= pd.Timestamp(min_date)) & (hour_df["dteday"] <= pd.Timestamp(max_date))]

# Menampilkan Penjelasan Otomatis Berdasarkan Tanggal
st.sidebar.markdown("### ℹ️ Informasi Data yang Dipilih")
st.sidebar.write(f"Data tersedia dari **{day_df['dteday'].min().strftime('%Y-%m-%d')}** hingga **{day_df['dteday'].max().strftime('%Y-%m-%d')}**")
st.sidebar.write(f"Anda memilih rentang tanggal dari **{min_date}** hingga **{max_date}**")

jumlah_hari = (pd.Timestamp(max_date) - pd.Timestamp(min_date)).days + 1
total_penyewaan_filtered = day_df_filtered['cnt'].sum()
rata_rata_penyewaan = total_penyewaan_filtered / jumlah_hari if jumlah_hari > 0 else 0

st.sidebar.write(f"Jumlah hari dalam rentang ini: **{jumlah_hari}** hari")
st.sidebar.write(f"Total penyewaan dalam rentang ini: **{total_penyewaan_filtered:,}** sepeda")
st.sidebar.write(f"Rata-rata penyewaan per hari: **{rata_rata_penyewaan:,.2f}** sepeda/hari")

# Perbandingan dengan Periode Sebelumnya
previous_period_end = pd.Timestamp(min_date) - pd.Timedelta(days=1)
previous_period_start = previous_period_end - pd.Timedelta(days=jumlah_hari - 1)
previous_df = day_df[(day_df["dteday"] >= previous_period_start) & (day_df["dteday"] <= previous_period_end)]
previous_total_penyewaan = previous_df['cnt'].sum()
change_percentage = ((total_penyewaan_filtered - previous_total_penyewaan) / previous_total_penyewaan * 100) if previous_total_penyewaan > 0 else 0


if halaman == "📅 Analisis Harian":
    st.subheader("📅 Analisis Penyewaan Sepeda Harian")
    fig = px.line(day_df_filtered, x="dteday", y="cnt", title="📈 Tren Penyewaan Sepeda Harian")
    st.plotly_chart(fig)

elif halaman == "⏰ Analisis Jam":
    st.subheader("⏰ Distribusi Penyewaan Sepeda Per Jam")
    fig = px.box(hour_df_filtered, x="hr", y="cnt", title="📊 Distribusi Penyewaan Sepeda Setiap Jam")
    st.plotly_chart(fig)

elif halaman == "☁️ Statistik Cuaca":
    st.subheader("☁️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
    fig = px.bar(
    day_df_filtered, 
    x="weathersit", 
    y="cnt", 
    title="🌦️ Pengaruh Kondisi Cuaca terhadap Penyewaan", 
    color="cnt", 
    color_continuous_scale="blues"  # Menggunakan skema warna biru
)

    st.plotly_chart(fig)
    st.markdown(
        """
        **Keterangan Kondisi Cuaca:**
        - 1️⃣ Cerah/Berawan sedikit
        - 2️⃣ Kabut + Berawan
        - 3️⃣ Hujan ringan/Snow ringan
        - 4️⃣ Hujan deras/Snow deras
        """)

    st.subheader(" Informasi lebih lanjut")
    st.write("**Rata-rata Suhu:**", f"{day_df['temp_C'].mean():.2f}°C")
    st.write("**Rata-rata Suhu yang Dirasakan:**", f"{day_df['atemp_C'].mean():.2f}°C")
    st.write("**Rata-rata Kelembaban:**", f"{day_df['humidity_percent'].mean():.2f}%")
    st.write("**Rata-rata Kecepatan Angin:**", f"{day_df['windspeed_kmh'].mean():.2f} km/h")

elif halaman == "📊 Analisis Lanjutan":
    st.subheader("🔍 Analisis Lanjutan")
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])

    latest_date = day_df['dteday'].max()
    rfm = day_df.groupby('dteday').agg({'cnt': 'sum', 'casual': 'sum', 'registered': 'sum'}).reset_index()
    rfm['Recency'] = (latest_date - rfm['dteday']).dt.days
    rfm['Frequency'] = 1
    rfm['Monetary'] = rfm['cnt']

    st.subheader("RFM Analysis")
    st.dataframe(rfm.head())

    def categorize_customer(monetary):
        if monetary < 500:
            return 'Low Usage'
        elif monetary <= 1500:
            return 'Regular User'
        else:
            return 'High Usage'

    rfm['Customer Category'] = rfm['Monetary'].apply(categorize_customer)
    customer_category_counts = rfm['Customer Category'].value_counts()
    
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
