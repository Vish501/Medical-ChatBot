from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone, ServerlessSpec

# Extract data from pdfs in the provided file directory
def pdf_extractor(directory):
    loader = DirectoryLoader(directory, glob="*.pdf", loader_cls=PyPDFLoader)
    return loader.load()


# Spliting data into chuncks
def text_split(data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    return splitter.split_documents(data)


# Loading embedding model
def embedding_loader():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


# Creating Pinecone DB
def create_db(api_key, db_name):
    pc = Pinecone(api_key = api_key)
    
    pc.create_index(
        name=db_name,
        dimension=384, # Size of the embeddings model output
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
