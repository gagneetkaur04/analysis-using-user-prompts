import os
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from plot_engine import plot_engine
from llama_index.core.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from prompt_template import new_prompt, instruction_str, context

def png_exists(directory='tempDir'):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            return True
    return False

def delete_png(directory='tempDir'):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)

# Answer questions about the data in a comprehensive and informative way
# def generate_response(df,query):
#     gemini_llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)
#     agent = create_csv_agent(gemini_llm, df, verbose=True)
#     response = agent.run(query)

#     return response
            
def generate_response(df, query, instruction_str=instruction_str, new_prompt=new_prompt):

    llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)
    csv_query_engine = PandasQueryEngine(df=df, llm=llm, verbose=True, instruction_str=instruction_str)
    csv_query_engine.update_prompts({"pandas_prompt": new_prompt})

    tools = [
        plot_engine,
        QueryEngineTool(
            query_engine=csv_query_engine,
            metadata=ToolMetadata(
                name="data",
                description="this gives information at the data present in CSV file",
            ),
        )
    ]

    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)         
    response = agent.query(query)

    return response

def save_uploadedfile(uploadedfile):
    with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    
    path = os.path.join("tempDir",uploadedfile.name)

    return path

def main():

    load_dotenv()
    API_KEY = os.environ['GOOGLE_API_KEY']
    genai.configure(api_key=API_KEY)

    st.set_page_config(page_title="Chat with your CSV")
    st.header("Chat with your CSV")

    uploaded_file = st.file_uploader("Upload a CSV file for analysis", type = ['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        path = save_uploadedfile(uploaded_file)

        prompt = st.text_area("Enter your prompt: ")

        if st.button('Generate'):
            delete_png()
            if prompt:
                if png_exists():
                    st.image('tempDir/output.png')
                else:
                    with st.spinner("Generating response..."):
                        st.write(generate_response(df, prompt))
            else:
                st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()