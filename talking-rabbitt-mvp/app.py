import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Talking Rabbitt", layout="wide")

st.title("🐰 Talking Rabbitt")
st.subheader("Conversational AI for your business data")

st.write("Upload a dataset and ask questions about your business.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about your data")

    if question:

        st.write("### AI Answer")

        if "region" in question.lower():

            result = df.groupby("Region")["Revenue"].sum()

            top_region = result.idxmax()
            top_value = result.max()

            st.write(f"The **{top_region}** region generated the highest revenue: **${top_value}**")

            st.write("### Revenue by Region")

            fig, ax = plt.subplots()

            result.plot(kind="bar", ax=ax)

            ax.set_ylabel("Revenue")

            st.pyplot(fig)

        elif "product" in question.lower():

            result = df.groupby("Product")["Revenue"].sum()

            best_product = result.idxmax()

            st.write(f"The highest revenue product is **{best_product}**")

            fig, ax = plt.subplots()

            result.plot(kind="bar", ax=ax)

            st.pyplot(fig)

        else:

            st.write("Try asking about **region revenue** or **product performance**.")