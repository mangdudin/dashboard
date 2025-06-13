import pandas as pd
import streamlit as st
import plotly.express as px

# === Load data dari Google Sheet ===
sheet_id = "1x8vyxmPH0ODEMcYdgCyvZvoSXTJKABZHx7-U_un1O04"
url_csv = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(url_csv)
df["total"] = df["jumlah"] * df["harga_satuan"]

# === Dashboard Streamlit ===
st.title("📊 Dashboard Penjualan via Google Spreadsheet")
st.metric("Total Pendapatan", f"Rp {df['total'].sum():,.0f}")

grafik = px.bar(df, x="produk", y="total", color="produk", title="Pendapatan per Produk")
st.plotly_chart(grafik)
