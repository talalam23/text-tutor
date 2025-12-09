"""
Utility functions for the Your Book Mentor application.
"""

import os
from typing import List, Dict, Any
import json
from datetime import datetime

def ensure_directory(directory: str) -> None:
    """
    Ensure a directory exists, create it if it doesn't.
    
    Args:
        directory: Path to the directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_conversation(question: str, answer: str, sources: List[str]) -> None:
    """
    Save a conversation to a JSON file.
    
    Args:
        question: The user's question
        answer: The AI's answer
        sources: List of source documents
    """
    ensure_directory("data/conversations")
    
    conversation = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer,
        "sources": sources
    }
    
    filename = f"data/conversations/conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(conversation, f, indent=2)

def load_conversations() -> List[Dict[str, Any]]:
    """
    Load all saved conversations.
    
    Returns:
        List of conversation dictionaries
    """
    conversations = []
    conversation_dir = "data/conversations"
    
    if os.path.exists(conversation_dir):
        for filename in os.listdir(conversation_dir):
            if filename.endswith(".json"):
                with open(os.path.join(conversation_dir, filename), "r", encoding="utf-8") as f:
                    conversations.append(json.load(f))
    
    return sorted(conversations, key=lambda x: x["timestamp"], reverse=True)

def format_source(source: str) -> str:
    """
    Format a source string for display.
    
    Args:
        source: The source string to format
        
    Returns:
        Formatted source string
    """
    if source == "direct_input":
        return "Direct Text Input"
    elif source.endswith(".pdf"):
        return f"PDF: {os.path.basename(source)}"
    return source 