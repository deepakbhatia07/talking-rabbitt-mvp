import streamlit as st
import pandas as pd

st.set_page_config(page_title="Talking Rabbitt", layout="wide")

st.title("🐰 Talking Rabbitt")
st.subheader("Conversational AI for your business data")

st.write("Upload a CSV dataset and ask questions about your data.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about your data")

    if question:

        if "region" in question.lower():

            result = df.groupby("Region")["Revenue"].sum()

            top_region = result.idxmax()
            top_value = result.max()

            st.success(f"Top region: **{top_region}** with revenue ${top_value}")

            st.write("### Revenue by Region")
            st.bar_chart(result)

        elif "product" in question.lower():

            result = df.groupby("Product")["Revenue"].sum()

            best_product = result.idxmax()

            st.success(f"Best product: **{best_product}**")

            st.write("### Revenue by Product")
            st.bar_chart(result)

        else:

            st.info("Try asking about **region revenue** or **product performance**.")
