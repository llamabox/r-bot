print("loading ollama...")
from llama_index.llms import Ollama
from llama_index import ServiceContext
from llama_index.readers import SimpleWebPageReader
from llama_index.response_synthesizers import TreeSummarize

llm = Ollama(model="mistral", request_timeout=30.0)
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")
print("DONE")


def doSummary(url):
    print(f"loading data from {url} ...")
    reader = SimpleWebPageReader(
        html_to_text=True
    )
    docs = reader.load_data([url])
    text = docs[0].text
    print("DONE")

    print("summarizing ...")
    summarizer = TreeSummarize(service_context=service_context,verbose=True)
    response =  summarizer.get_response("what is all about?", [text])
    return(response)

if __name__=='__main__':
    url='https://smartcontract.tips/articoli/cosa-sono-gli-smart-contract-definizione-ed-esempi/'
    print(doSummary(url))