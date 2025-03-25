from src.helper import pdf_extractor, text_split, embedding_loader, create_db
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore

import sys
import os

def main():
    # Moving 1 directory up to directly access the data folder
    os.chdir("../")

    # Loading environment variables
    load_dotenv()
    os.environ["PINECONE_API_KEY"] = os.environ.get("PINECONE_API_KEY")

    # Extracting data from data folder and turning it into chunks
    extracted_data = pdf_extractor("data/")
    chunks = text_split(extracted_data)

    # Initializing the embedding model
    embeddings = embedding_loader()

    db_name = "medibot"
    # Initializing and setting up the Pinecone database for use if CLI create passed
    if sys.argv[1] == "create":
        create_db(os.environ["PINECONE_API_KEY"], db_name)

    # Adding each chunk and its embedding into Pinecone database initialized earlier as indexes
    PineconeVectorStore.from_documents(
        documents=chunks,
        index_name=db_name,
        embedding=embeddings
    )


if __name__ == "__main__":
    main()
