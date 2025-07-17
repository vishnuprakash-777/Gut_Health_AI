import os
import json
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import JSONLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI  

load_dotenv()

def load_jsonl(file_path):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            if line.strip():  # skip empty lines
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Skipping invalid line: {line.strip()} — {e}")
    return data

def build_vectorstore(data_path="gut_health_qa_dataset.jsonl"):
    data = load_jsonl(data_path)
    text_data = [f"Q: {item['instruction']}\nA: {item['response']}" for item in data]
    docs = [doc for doc in text_data]

    embeddings = HuggingFaceEmbeddings()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.create_documents(docs)

    vectorstore = FAISS.from_documents(split_docs, embeddings)
    return vectorstore

def get_rag_chain():
    retriever = build_vectorstore().as_retriever()

    system_prompt = """
    You are a compassionate and science-backed gut health coach. 
    Answer in a warm, kind, and non-judgmental tone. Avoid jargon unless explained.

   Example tone:
    - “It’s okay — this happens to a lot of people.”
    - “Your concern is valid, and here’s what we can look into.”
    - “You’re not alone — many people experience this.”
    - “Let’s gently explore what might be going on.”
    - “There’s no shame in this — your body’s just sending signals.”
    - “You’re doing the right thing by paying attention to your health.”
    - “You’re being proactive — that’s already a great first step.”
    - “Healing isn’t always linear, but every step matters.”
    - “Thanks for sharing that — it’s brave to ask about something so personal.”
    - “Let’s look at what might help, without overwhelming you.”
    - “It’s okay to not feel okay sometimes. We can figure this out together.”
    - “Your symptoms are valid, and there are gentle ways to support healing.”

    {context}
    Question: {question}
    Answer:
    """

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=system_prompt.strip()
    )

    # ✅ Use Mistral API directly
    llm = ChatMistralAI(
        model="mistral-small-latest",  # or mistral-medium, etc.
        temperature=0.3,
        mistral_api_key=os.getenv("MISTRAL_API_KEY")
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain
