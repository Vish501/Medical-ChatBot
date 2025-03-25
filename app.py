from Flask import Flask, render_template, jsonify, requests
from src.helper import embedding_loader
from src.prompt import sys_prompt
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

import os

load_dotenv()
os.environ["PINECONE_API_KEY"] = os.environ.get("PINECONE_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.environ.get("GENAI_API_KEY")

