import streamlit as st
import pandas as pd

st.title("AI Data Analyst")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df)

    st.subheader("Dataset Information")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("Select Column For Analysis")

    numeric_columns = df.select_dtypes(include="number").columns

    selected_column = st.selectbox("Choose a column", numeric_columns)

    st.write("Average:", df[selected_column].mean())
    st.write("Maximum:", df[selected_column].max())
    st.write("Minimum:", df[selected_column].min())

    chart_type = st.selectbox(
    "Choose Chart Type",
    ["Bar Chart", "Line Chart"]
    )

if chart_type == "Bar Chart":
    st.bar_chart(df[selected_column])

elif chart_type == "Line Chart":
    st.line_chart(df[selected_column])

    st.subheader("Missing Values")

st.write(df.isnull().sum())

st.subheader("Dataset Summary")

st.write(df.describe())

st.subheader("Correlation Matrix")

st.write(df.corr(numeric_only=True))

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    "processed_data.csv",
    "text/csv"
)