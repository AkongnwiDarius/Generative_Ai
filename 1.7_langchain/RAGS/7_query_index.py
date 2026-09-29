import time

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from torch import embedding

# Load persisted vectore store
start = time.perf_counter()
embeddings = HuggingFaceEmbeddings(
    model_name = 'sentence-transformers/all-MiniLM-l6-v2'
)

vector_store = Chroma(
    persist_directory = "./chroma_db",
    embedding_function = embeddings
)
reload_time = time.perf_counter() - start

#perform similiarity search
query_start = time.perf_counter()
results = vector_store.similarity_search('What is fog computing', k=3)
query_time = time.perf_counter() - query_start

#Display results
print(f'Reloaded persistent index in {reload_time:.3f} seconds (no re-embedding of documents)')
print(f'Query took {query_time:.3f} seconds')
for doc in results:
    print(f'- {doc.page_content[:100]}...')

