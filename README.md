# Rag PoC with LLamaIndex

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
pip install llama-index
pip install flask
pip install flask_cors
pip install transformers
pip install torch
pip install pypdf
```
Don't forget to install Ollama and launch it

https://github.com/ollama/ollama


Then run the app
```
flask --app teller.app  run
```

You can now connect to 
```
http://127.0.0.1:5000/
```
