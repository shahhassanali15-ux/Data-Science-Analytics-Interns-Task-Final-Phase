import streamlit as st
import pandas as pd

df = pd.read_csv("superstore.csv")

st.title("📊 Sales Dashboard")

st.write("Total Sales:", df["Sales"].sum())
st.write("Total Profit:", df["Profit"].sum())
