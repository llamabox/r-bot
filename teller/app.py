
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect
from flask_cors import CORS
from llama_index.llms import Ollama
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
import json

#os.environ['OPENAI_API_KEY'] = open(".openai").read().strip()

# Setup llamaindex here

llm = Ollama(model="mistral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")


documents = SimpleDirectoryReader("docs").load_data()
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

query_engine = index.as_query_engine()




# From here is Flask

app = Flask(__name__)
CORS(app)



@app.route('/')
def home():
    return redirect("/static/index.html", code=302)

@app.route('/chat')
def chat():
    return redirect("/static/chat/index.html", code=302)


@app.route('/ask')
def ask():
    question = request.args.get('q')
    completion = query_engine.query(question)
    return f"{question} ,  {completion}"

@app.route('/postQuestion',  methods=['POST'])
def postQuestion():
    question = request.form['q']
    completion = query_engine.query(question)
    return f"{completion}"

# route with openAI syntax
@app.route('/v1/chat/completions',  methods=['POST'])
def completions():
    payload = request.json
    print(f"payload: {payload}")
    question = payload["messages"][0]["content"]
    print(question)

    answer = query_engine.query(question)
    print("** ANSWER **")
    print(answer)

    # Creazione del JSON
    data = {
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": str(answer)
                }
            }
        ]
    }


    return json.dumps(data)

"""
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "ciao"
    }
  ],
  "max_tokens": 2048,
  "temperature": 0.2,
  "n": 1,
  "stop": null
}

response.choices[0].message.content.trim();
"""