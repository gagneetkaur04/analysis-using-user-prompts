import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.environ['GOOGLE_API_KEY']
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

# -------------------------------- STREAMLIT --------------------------------------
st.title("Prompt-driven analysis with PandasAI")
uploaded_file = st.file_uploader("Upload a CSV file for analysis", type = ['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write('------------------------------DATA--------------------------------')
    st.write(df.head(3))
    st.write('---------------------------STATISTICS------------------------------')
    st.write('Mean')
    st.write(df.mean())
    st.write('Median')
    st.write(df.median())

    prompt = st.text_area("Enter your prompt: ")

    if st.button('Generate'):
        if prompt:
            with st.spinner("Generating response..."):
                st.write("--response--")
        else:
            st.warning("Please enter a prompt.")