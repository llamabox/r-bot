# Rag PoC with LLamaIndex

## Note
This branch is about using Mistral and Ollama based on this [blog post instructions](https://blog.llamaindex.ai/running-mixtral-8x7-locally-with-llamaindex-e6cebeabe0ab)

## Instructions

Create a python environment and activate it

```
python -m venv .flaskenv
source .flaskenv/bin/activate
```

Upgrade pip 
```
pip install --upgrade pip
```

Then install Flask and the other dependencies

```
pip install flask
pip install flask_cors
pip install llama_index
pip install pypdf
```
Then run the app
```
flask --app teller.app  run
```

You can now connect to 
```
http://127.0.0.1:5000/
```
