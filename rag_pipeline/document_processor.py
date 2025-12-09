"""
Document processing module for handling PDFs and text input.
"""

import os
from typing import List, Union
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def process_document(uploaded_file) -> None:
    """
    Process an uploaded PDF document and store it in the vector database.
    
    Args:
        uploaded_file: The uploaded PDF file from Streamlit
    """
    # Save the uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())
    
    # Load and process the PDF
    loader = PyPDFLoader("temp.pdf")
    pages = loader.load()
    
    # Clean up temporary file
    os.remove("temp.pdf")
    
    # Process the pages
    process_text_chunks(pages)

def process_text(text: str) -> None:
    """
    Process input text and store it in the vector database.
    
    Args:
        text: The input text to process
    """
    from langchain.schema import Document
    doc = Document(page_content=text, metadata={"source": "direct_input"})
    process_text_chunks([doc])

def process_text_chunks(documents: List) -> None:
    """
    Process text chunks and store them in the vector database.
    
    Args:
        documents: List of Document objects to process
    """
    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=int(os.getenv("CHUNK_SIZE", 1000)),
        chunk_overlap=int(os.getenv("CHUNK_OVERLAP", 200)),
        length_function=len,
    )
    
    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)
    
    # Initialize embeddings
    embeddings = OpenAIEmbeddings()
    
    # Create or update vector store
    if st.session_state.vectorstore is None:
        st.session_state.vectorstore = FAISS.from_documents(chunks, embeddings)
    else:
        st.session_state.vectorstore.add_documents(chunks)
    
    # Update session state
    st.session_state.documents.extend(chunks) 