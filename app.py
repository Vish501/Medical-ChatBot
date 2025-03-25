from flask import Flask, render_template, jsonify, request
from src.helper import embedding_loader
from src.prompt import sys_prompt
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

import os

db_name = "medibot"

# Loading environment variables
load_dotenv()
os.environ["PINECONE_API_KEY"] = os.environ.get("PINECONE_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.environ.get("GENAI_API_KEY")

# Loading embeddings model
embeddings = embedding_loader()

# Loading data from DB
doc_search = PineconeVectorStore.from_existing_index(
    index_name=db_name,
    embedding=embeddings
)

# Initializing required objectss
retriever = doc_search.as_retriever(search_type="similarity", search_kwargs={"k":3}) # Initializing retriever object
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0, max_retries=2) # Initializing LLM

# Constructing prompt to be used in chain
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", sys_prompt),
        ("human", "{input}")
    ]
)

# Initializing prompt chain
chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, chain)

# Setting up flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chatbot.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    message = request.form["msg"]
    print(f"Question: {message}")

    response = rag_chain.invoke({"input": message})
    print(f"Response: {response['answer']}")

    return response['answer']


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
