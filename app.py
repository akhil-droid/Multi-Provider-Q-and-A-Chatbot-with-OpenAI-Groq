import openai
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT_NAME"]= "Q&A Chatbot"
os.environ["LANGCHAIN_TRACING_v2"]= "true"

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","you are an helpful assistant, so please answer the user questions"),
        ("user","Questions:{input}")
    ]
)

def get_response(input, api_key, llm_model, temperature, max_tokens):
    os.environ["OPENAI_API_KEY"] = api_key
    llm = ChatOpenAI(model=llm_model, temperature=temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"input": input})
    return answer


# title
st.title("Enhanced Q&A chatbot with OPENAI")

# side bar
st.sidebar.title("Settings")

# openai api key
api_key= st.sidebar.text_input("Enter your OpenAI api key", type="password")

# dropdown to select the model
llm= st.sidebar.selectbox("Select an OpenAI model",["gpt-4o", "gpt-4-turbo", "gpt-4"])


# slider for temperature and max_tokens
temperature= st.sidebar.slider("Temperature", max_value=1.0, min_value=0.0, value=0.7)
max_tokens= st.sidebar.slider("Max_tokens", max_value=300, min_value=100, value=150)

#main interface for the user input
st.write("Go ahead and ask your question")
query= st.text_input("you:")

if query:
    response= get_response(query, api_key, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("provide the query")

