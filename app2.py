import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

# Load .env
load_dotenv()
os.environ["LANGSMITH_API_KEY"]= os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"]= os.getenv("LANGSMITH_PROJECT")
os.environ["LANGSMITH_TRACING"]= os.getenv("LANGSMITH_TRACING")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the user's questions."),
    ("user", "Question: {input}")
])

# Function to route based on provider
def get_response(input, provider, api_key, model, temperature, max_tokens):
    if provider == "OpenAI":
        os.environ["OPENAI_API_KEY"] = api_key
        llm = ChatOpenAI(model=model, temperature=temperature, max_tokens=max_tokens)
    elif provider == "Groq":
        os.environ["GROQ_API_KEY"] = api_key
        llm = ChatGroq(model=model, temperature=temperature, max_tokens=max_tokens)
    else:
        return "Invalid provider selected."
    
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # from langchain.callbacks.tracers import LangChainTracer
    # tracer = LangChainTracer()
    # config={"callbacks": [tracer]}

    answer = chain.invoke({"input": input} )
    return answer

# Streamlit UI
st.title("Multi-Provider Q&A Chatbot (OpenAI + Groq)")

# Sidebar inputs
st.sidebar.title("Settings")

provider = st.sidebar.selectbox("Select Provider", ["OpenAI", "Groq"])

if provider == "OpenAI":
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
    model = st.sidebar.selectbox("Model", ["gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"])
elif provider == "Groq":
    api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")
    model = st.sidebar.selectbox("Model", ["Gemma-7b-it", "Mixtral-8x7b", "LLaMA3-8b"])

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 100, 1000, 300)

# Main input
st.write("Ask your question:")
query = st.text_input("You:")

# Handle query
if query:
    if not api_key:
        st.warning(" Please enter your API key.")
    else:
        with st.spinner("Generating response..."):
            response = get_response(query, provider, api_key, model, temperature, max_tokens)
            st.success("Response:")
            st.write(response)
