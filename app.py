import pandas as pd
import streamlit as st
import plotly.express as px

# ========== CONFIG ==========
SPREADSHEET_ID = "1x8vyxmPH0ODEMcYdgCyvZvoSXTJKABZHx7-U_un1O04"
SHEET_NAME = "Sheet1"  # Contoh: "Sheet1"

# ========== LOAD DATA ==========
csv_url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
df = pd.read_csv(csv_url)

# Hitung total
df["total"] = df["jumlah"] * df["harga_satuan"]

# ========== DASHBOARD ==========
st.set_page_config(page_title="Dashboard Penjualan", layout="wide")
st.title("📊 Dashboard Penjualan dari Google Spreadsheet")

# Info pendapatan total
st.metric(label="Total Pendapatan", value=f"Rp {df['total'].sum():,.0f}")

# Grafik pendapatan per produk
grafik_produk = px.bar(df, x="produk", y="total", color="produk", title="Pendapatan per Produk")
st.plotly_chart(grafik_produk, use_container_width=True)

# Grafik tren harian
grafik_tren = px.line(df.groupby("tanggal")["total"].sum().reset_index(),
                      x="tanggal", y="total", title="Pendapatan Harian")
st.plotly_chart(grafik_tren, use_container_width=True)

# Tabel data
st.subheader("🧾 Data Penjualan Lengkap")
st.dataframe(df)
