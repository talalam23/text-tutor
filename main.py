"""
Main entry point for the Text Tutor application.
Launches the Streamlit interface and initializes the RAG pipeline.
"""

import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Text Tutor",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application entry point."""
    st.title("📚 Text Tutor")
    st.markdown("""
    Welcome to Text Tutor! Upload your documents or input text,
    and get AI-powered insights and answers to your questions.
    """)

    # Initialize session state
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None
    if "documents" not in st.session_state:
        st.session_state.documents = []

    # Sidebar for document upload
    with st.sidebar:
        st.header("Document Upload")
        uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
        if uploaded_file:
            # Process the uploaded file
            from rag_pipeline.document_processor import process_document
            process_document(uploaded_file)
            st.success("Document processed successfully!")

        st.header("Text Input")
        text_input = st.text_area("Or enter text directly", height=200)
        if text_input and st.button("Process Text"):
            from rag_pipeline.document_processor import process_text
            process_text(text_input)
            st.success("Text processed successfully!")

    # Main content area
    st.header("Ask Questions")
    question = st.text_input("What would you like to know about your documents?")
    
    if question and st.button("Get Answer"):
        if not st.session_state.vectorstore:
            st.warning("Please upload a document or enter text first!")
        else:
            from rag_pipeline.qa_chain import get_answer
            with st.spinner("Thinking..."):
                answer, sources = get_answer(question)
                
                st.subheader("Answer")
                st.write(answer)
                
                if sources:
                    st.subheader("Sources")
                    for source in sources:
                        st.markdown(f"- {source}")

if __name__ == "__main__":
    main() 