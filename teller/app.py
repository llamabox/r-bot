
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect
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
    return redirect("/static/index.html", code=302)



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


