# 🦠 Gut Health Coach AI

A personalized AI-powered assistant to answer your gut health queries with science-backed, empathetic responses — just like talking to a wellness coach. Built as part of a GenAI Internship Task



---

## 🧠 Features

- **Conversational Q&A** on digestion, bloating, probiotics, SIBO, sugar cravings, and more.
- **RAG-based architecture**: Retrieval-Augmented Generation using LangChain + FAISS vector store.
- **Contextual, non-judgmental tone** inspired by August AI.
- **Powered by**: Mistral API, Hugging Face embeddings, Streamlit, LangChain.

---

## 🧪 Technology Stack

- Python 3.12+
- Streamlit
- LangChain
- Mistral API (via `langchain-mistralai`)
- Hugging Face Embeddings
- FAISS for vector search

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/vishnuprakash-777/gut_health_ai.git
cd gut_health_ai
```

### 2. Create & Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add:

```
MISTRAL_API_KEY=your_mistral_api_key_here
```

⚠️ **Never commit your .env file or API keys to GitHub!**

### 5. Run the App Locally

```bash
streamlit run streamlit_app.py
```

---

## 🌐 Live Deployment

The project is live here 👉 [https://guthealthai-bsajprsbwksqqczagzueax.streamlit.app](https://guthealthai-bsajprsbwksqqczagzueax.streamlit.app)

---

## 🧬 Example Questions It Can Answer

- I've been bloated for 3 days — what should I do?
- Can antibiotics damage gut flora permanently?
- Why do I feel brain fog after eating sugar?
- Should I fast if my gut is inflamed?
- What are signs that my gut is healing?

---

## 📦 Project Structure

```
gut_health_ai/
├── streamlit_app.py             # Main Streamlit interface
├── rag_gut_health.py            # RAG logic with Mistral
├── gut_health_qa_dataset.jsonl  # Fine-tuned Q&A dataset
├── requirements.txt
└── .env                         # Environment variables (not committed)
```