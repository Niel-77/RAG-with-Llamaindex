# Import modules
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

import ollama
from llama_index.llms.ollama import Ollama
from pathlib import Path
import qdrant_client
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, ServiceContext, StorageContext, Settings
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding

# Create Qdrant client and store
# client = qdrant_client.QdrantClient(path="./Rag_data")
# vector_store = QdrantVectorStore(client=client, collection_name="Queries")
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# Initialize Ollama and ServiceContext
Settings.llm = Ollama(model="phi3:mini",request_timeout=600,device_map='cuda')
Settings.embed_model= OllamaEmbedding(model_name="nomic-embed-text")

# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("Research_Papers").load_data()
    #Split the documents
    
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# Either way we can now query the index
query_engine = index.as_query_engine()
response = query_engine.query("Give me the summary of the paper.")
print(response)


