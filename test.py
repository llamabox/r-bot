from llama_index.llms import Ollama
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext


llm = Ollama(model="mistral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")


documents = SimpleDirectoryReader("docs").load_data()
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

query_engine = index.as_query_engine()
response = query_engine.query(
    "Write an email to the user given their background information."
)
print(response)