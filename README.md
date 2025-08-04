# 🔮 Multi-Provider Q&A Chatbot (OpenAI + Groq)

An interactive chatbot built using **Streamlit** and **LangChain**, supporting both **OpenAI** and **Groq** large language models. This app allows you to switch between providers and models like `gpt-4o`, `Mixtral`, `Gemma`, and more — all from a user-friendly interface.

---

## ✨ Features

- 🔁 **Choose between OpenAI and Groq models**
- 🧠 Works with `gpt-4o`, `gpt-4`, `gpt-3.5-turbo`, `Mixtral`, `Gemma`, `LLaMA3`, etc.
- ⚙️ Adjustable `temperature` and `max_tokens` in real time
- 🔐 Secure API key input via sidebar
- 💡 Uses `LangChain`, `ChatPromptTemplate`, and `Streamlit` for a modular design

---

## 🚀 Getting Started

### 1. Clone the Repository
git clone https://github.com/akhilsalla/multi-provider-qa-chatbot.git
cd multi-provider-qa-chatbot

### 2. Install Dependencies
Make sure you have Python 3.8+ and pip installed.
pip install -r requirements.txt

### 3. Create a .env File (Optional)
If you want to set a default LangChain API key:
LANGCHAIN_API_KEY=your_langchain_key

### 4. Run the App
streamlit run app.py

---

🧪 How to Use
1. Open the app in your browser.

2. Choose a provider: OpenAI or Groq.

3. Paste your API key for the selected provider.

4. Select your preferred model.

5. Adjust temperature and token limit if needed.

6. Enter a question in the text box and see the response!

---

🛠️ Models Supported
✅ OpenAI
. gpt-4o

. gpt-4-turbo

. gpt-4

. gpt-3.5-turbo

✅ Groq
. Mixtral-8x7b

. Gemma-7b-it

. LLaMA3-8b
