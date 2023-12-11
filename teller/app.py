
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template
from flask_cors import CORS
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os

os.environ['OPENAI_API_KEY'] = open(".openai").read().strip()

app = Flask(__name__)
CORS(app)

documents = SimpleDirectoryReader("docs").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

@app.route('/')
def home():
    return open('templates/index.html').read()


@app.route('/x')
def tell():
    completion = query_engine.query("What did the author do growing up?")
    #print(completion)
    return str(completion)


@app.route('/ask')
def ask():
    question = request.args.get('q')
    completion = query_engine.query(question)
    return f"{question} ,  {completion}"

@app.route('/postQuestion',  methods=['POST'])
def postQuestion():
    question = request.form['q']
    completion = query_engine.query(question)
    return f"{question} : {completion}"


