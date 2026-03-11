import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Talking Rabbitt", layout="wide")

st.title("🐰 Talking Rabbitt")
st.subheader("Conversational AI for your business data")

st.write("Upload a dataset and ask questions about it.")

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

            st.success(f"The region with highest revenue is **{top_region}** with ${top_value}")

            fig = px.bar(
                x=result.index,
                y=result.values,
                labels={"x":"Region","y":"Revenue"},
                title="Revenue by Region"
            )

            st.plotly_chart(fig)

        elif "product" in question.lower():
            result = df.groupby("Product")["Revenue"].sum()

            best_product = result.idxmax()

            st.success(f"The highest revenue product is **{best_product}**")

            fig = px.bar(
                x=result.index,
                y=result.values,
                labels={"x":"Product","y":"Revenue"},
                title="Revenue by Product"
            )

            st.plotly_chart(fig)

        else:
            st.info("Try asking about **region revenue** or **product performance**.")
