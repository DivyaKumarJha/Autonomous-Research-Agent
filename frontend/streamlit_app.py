import streamlit as st
import requests

st.title("Autonomous Research Agent")

query = st.text_input("Enter research question")

if st.button("Run Research"):

    response = requests.post(
        "http://localhost:8000/research",
        params={"query": query}
    )

    result = response.json()

    st.write(result)