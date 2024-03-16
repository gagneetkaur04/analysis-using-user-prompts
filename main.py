import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import google.generativeai as genai
from dotenv import load_dotenv
from llama_index.core.query_engine import PandasQueryEngine
from pandasai import SmartDataframe
from pandasai.llm.google_palm import GooglePalm
from langchain_google_genai import ChatGoogleGenerativeAI


# statistical analysis like mean, median, mode, std dev, etc.
def analyze_data(df):
    pass

# plots related to data
def generate_plot(df, col_name, plot_type):
    plt.show()

# response generation of llm
def generate_response(file_path, query, temperature=0.5):
    df = pd.read_csv(file_path)
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=temperature)

    pdi = SmartDataframe(df, config={"llm": llm})
    
    return pdi.chat(query)


def main():

    # Load Environment Variables
    load_dotenv()
    API_KEY = os.environ['GOOGLE_API_KEY']
    genai.configure(api_key=API_KEY)

    # App Title
    st.title("Prompt-driven analysis with PandasAI")

    # Storing the user uploaded csv
    uploaded_file = st.file_uploader("Upload a CSV file for analysis", type = ['csv'])

    # Performing Statistical Analysis on CSV and Prompt Generation
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        prompt = st.text_area("Enter your prompt: ")

        if st.button('Generate'):
            if prompt:
                with st.spinner("Generating response..."):
                    st.write("--response--")
            else:
                st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()