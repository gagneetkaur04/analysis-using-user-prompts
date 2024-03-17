import os
import pandas as pd
import seaborn as sns
import streamlit as st
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import google.generativeai as genai
import matplotlib.axes._axes as axes_module
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_csv_agent

def generate_response(path,query):
    gemini_llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)
    agent = create_csv_agent(gemini_llm, path, verbose=True, return_intermediate_steps=True)
    response = agent.invoke({"input": query})

    return response

def save_uploadedfile(uploadedfile):
    if not os.path.exists('tempDir'):
        os.makedirs('tempDir')

    with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    
    path = os.path.join("tempDir",uploadedfile.name)

    return path

def plot_exists(text: dict):
    if isinstance(text['output'], axes_module.Axes):
        return text['output'].get_figure()
    steps = text['intermediate_steps']
    for step in steps:
        if isinstance(step[1], axes_module.Axes):
            fig = step[1]
            return fig.get_figure()
    return text['output']

def main():

    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)


    st.set_page_config(page_title="Chat with your CSV")
    st.header("Chat with your CSV")

    uploaded_file = st.file_uploader("Upload a CSV file for analysis", type = ['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        path = save_uploadedfile(uploaded_file)
        st.dataframe(df)

        prompt = st.text_area("Enter your prompt: ")

        if st.button('Generate'):
            if prompt:
                with st.spinner("Generating response..."):
                    result = generate_response(path, prompt)
                    st.write(plot_exists(result))
            else:
                st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()