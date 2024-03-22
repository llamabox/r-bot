print("loading ollama...")
from llama_index.llms import Ollama
from llama_index import ServiceContext
llm = Ollama(model="mistral", request_timeout=20.0)
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")
print("DONE")



print("loading data ...")
from llama_index import SimpleDirectoryReader
reader = SimpleDirectoryReader(
    input_files=["../docs/dichiarazione-voto.txt"]
)
docs = reader.load_data()
text = docs[0].text
print(text)


print("summarizing ...")
from llama_index.response_synthesizers import TreeSummarize
summarizer = TreeSummarize(service_context=service_context,verbose=True)
prompt="""
this is a parlamentary assembly where the speaker named Lombardo, asks to speak and then express his opinions on a subject.  
Please summarize the speech of the speaker and then answer whether he 
vote in favour or against the proposed motion?
Produce answer in Italian.
"""
response =  summarizer.get_response(prompt, [text])
print(response)