import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
)
from llama_index.llms import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore

client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)
vector_store = QdrantVectorStore(client=client, collection_name="tweets")

llm = Ollama(model="mistral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")

index = VectorStoreIndex.from_vector_store(vector_store=vector_store,service_context=service_context)
query_engine = index.as_query_engine(similarity_top_k=20)
response = query_engine.query("Does the author like SQL? Give details.")
print(response)