import dotenv
import time
from langchain_core.tools import tool
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_chroma import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings
from core.ingestion import load_and_split_folder, load_documents
from torch import embedding
from RAGS.f1_similarity_search import cosine_similarity
from RAGS.f3_chunking import load_folder

from dotenv import load_dotenv

@tool
def smart_retrieval_tool(query: str, folder_path: str, k: int = 3) -> list:
    """
    A tool that performs semantic search on documents in a folder and returns the top k relevant documents.
    
    Args:
        query (str): The query string to search for.
        folder_path (str): The path to the folder containing documents.
        k (int): The number of top relevant documents to return. Default is 3.
        
    Returns:
        list: A list of the top k relevant documents.
    """
    # Load and split documents from the specified folder
    all_chunks = load_and_split_folder(folder_path)
    
    # Initialize embeddings model
    embeddings_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-l6-v2')
    
    # Create an in-memory vector store and add document chunks
    vector_store = InMemoryVectorStore(embedding=embeddings_model)
    vector_store.add_documents(all_chunks)
    
    # Perform similarity search
    results = vector_store.similarity_search(query, k=k)
    
    return results


