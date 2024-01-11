from pathlib import Path
import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    download_loader,
    SimpleDirectoryReader
)
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore

# Assign the name for the collection, it must be a directory with the same
# name containing the files to be loaded
# kbase = 'kbase-paulgraham'
kbase = 'kbase-rmassimo'
loader = SimpleDirectoryReader(kbase)






# Modify with the proper path
#path = Path('tinytweets.json')
documents = loader.load_data()

client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)

vector_store = QdrantVectorStore(client=client, collection_name=kbase)
storage_context = StorageContext.from_defaults(vector_store=vector_store)


# Select your model, eg. mistral
llm = Ollama(model="mistral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")

index = VectorStoreIndex.from_documents(documents,service_context=service_context,storage_context=storage_context)

query_engine = index.as_query_engine()

# Prepare your smoke test question
# "What is the name of the author's dog"
response = query_engine.query("What does the author think about Kids? Give details.")
print(response)