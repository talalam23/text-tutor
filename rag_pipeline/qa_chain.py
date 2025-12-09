"""
Question-answering chain module for handling user queries.
"""

import os
from typing import Tuple, List
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_answer(question: str) -> Tuple[str, List[str]]:
    """
    Get an answer to a question using the RAG pipeline.
    
    Args:
        question: The user's question
        
    Returns:
        Tuple containing the answer and list of sources
    """
    # Initialize the LLM
    llm = ChatOpenAI(
        model_name=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
        temperature=float(os.getenv("TEMPERATURE", 0.7)),
        max_tokens=int(os.getenv("MAX_TOKENS", 1000))
    )
    
    # Initialize conversation memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # Create the QA chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=st.session_state.vectorstore.as_retriever(
            search_kwargs={"k": 3}
        ),
        memory=memory,
        return_source_documents=True
    )
    
    # Get the answer
    result = qa_chain({"question": question})
    
    # Extract answer and sources
    answer = result["answer"]
    sources = [doc.metadata.get("source", "Unknown") for doc in result["source_documents"]]
    
    return answer, sources 