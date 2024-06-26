import qdrant_client
from llama_index.core import VectorStoreIndex, ServiceContext
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding
import httpx

client = httpx.Client(timeout=httpx.Timeout(300.0))  # Increase timeout to 30 seconds


# Create Qdrant client and vector store
client = qdrant_client.QdrantClient(path="./Rag_data")
vector_store = QdrantVectorStore(client=client, collection_name="Queries")

# Initialize Ollama and ServiceContext
Settings.llm = Ollama(model="phi3:mini")
Settings.embed_model=OllamaEmbedding(model_name="nomic-embed-text")
service_context = ServiceContext.from_defaults(llm=Settings.llm, embed_model=Settings.embed_model)

# Create VectorStoreIndex and query engine with a similarity threshold of 20
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, service_context=service_context)
query_engine = index.as_query_engine(similarity_top_k=20)

# Perform a query and print the response
response = query_engine.query("What is the main outcome of the paper? In One line")
print(response)

#This is not working. Gives time out error.