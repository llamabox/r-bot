
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect
from flask_cors import CORS
import fromURL
import json

# From here is Flask

app = Flask(__name__)
CORS(app)



@app.route('/')
def home():
    return redirect("/static/index.html", code=302)

@app.route('/hello')
def hello():
    return "hello!"


@app.route('/summarize',methods=['POST'])
def doSummary():
    url = request.form['url']
    print(f"url is {url}")
    summary = fromURL.doSummary(url)
    #summary = "Ciao"
    data={
        "url"    : url,
        "summary": summary
    }
    return json.dumps(data)
   


