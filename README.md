# Text Tutor

A powerful RAG-based application that helps users interact with their books and documents through natural language queries.

## Features

- Upload PDF documents or input text directly
- Advanced document processing with chunking and embedding
- Intelligent question answering using RAG (Retrieval-Augmented Generation)
- Powered by state-of-the-art LLMs (OpenAI GPT or HuggingFace models)
- Real-time streaming responses
- User-friendly Streamlit interface
- Docker support for easy deployment

## Project Structure

```
text-tutor/
├── app/                    # Streamlit frontend application
├── rag_pipeline/          # Document processing and RAG implementation
├── models/                # LLM integration and model management
├── utils/                 # Helper functions and utilities
├── tests/                 # Test files
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
├── Dockerfile           # Docker configuration
└── .env.example         # Environment variables template
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/talalam23/text-tutor.git
cd text-tutor
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```

5. Run the application:
```bash
python main.py
```

## Usage

1. Launch the application using `python main.py`
2. Access the web interface at `http://localhost:8501`
3. Upload your PDF documents or input text
4. Ask questions about your documents
5. Get AI-powered responses with source citations

## Docker Deployment

Build and run using Docker:

```bash
docker build -t text-tutor .
docker run -p 8501:8501 text-tutor
```

## Environment Variables

Create a `.env` file with the following variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `HUGGINGFACE_API_KEY`: Your HuggingFace API key (if using HF models)
- `VECTOR_DB_PATH`: Path to store vector database files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
