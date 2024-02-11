print("loading ollama...")
from llama_index.llms import Ollama
from llama_index import ServiceContext
llm = Ollama(model="mistral", request_timeout=10.0)
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")
print("DONE")



print("loading data ...")
from llama_index import SimpleDirectoryReader
reader = SimpleDirectoryReader(
    input_files=["../docs/essay.txt"]
)
docs = reader.load_data()
text = docs[0].text
print("DONE")


print("summarizing ...")
from llama_index.response_synthesizers import TreeSummarize
summarizer = TreeSummarize(service_context=service_context,verbose=True)
response =  summarizer.get_response("what is all about?", [text])
print(response)