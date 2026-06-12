# Langchain 
https://docs.langchain.com/oss/python/langchain/overview

* langchain github :
https://github.com/langchain-ai

# UV package manager installations
https://docs.astral.sh/uv/getting-started/installation/

* Install UV package maanger:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

* Initialize uv:
C:\Users\Admin\.local\bin\uv.exe init
ie. path\uv.exe init

OR 

uv init

# Create virtual environment:
C:\Users\Admin\.local\bin\uv.exe venv

# check uv version: 
C:\Users\Admin\.local\bin\uv.exe --version

# activate virtual environment
.venv/Scripts/activate

*****************************
cd D:\AGENTIC_AI_PROJECTS\AGENTIC_AI

python -m venv .venv

.venv\Scripts\activate

pip install ipykernel
python -m ipykernel install --user --name agentic_ai --display-name "Python (agentic_ai)"
*****************************

* uv add ipykernel

* uv add <library_name>

* uv add -r requirements.txt


### Best setup for learning LangChain/LangGraph

#### Option 1: Ollama (Recommended)

Install Ollama:

[Ollama Official Website](https://ollama.com?utm_source=chatgpt.com)

Then pull a model:

```bash
ollama pull llama3.2
```

Install packages: (in venv)

```bash
pip install langchain-ollama
pip install langgraph
pip install langchain
```

Verify

```bash
pip list
```

Make sure Ollama is running

```bash
ollama list
```

Test:

```python
from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2")

response = model.invoke("What is Agentic AI?")
print(response.content)
```

Benefits:

* No API costs
* No daily quotas
* Works perfectly with LangGraph memory, agents, tools, and RAG
* Great for experimentation

---
