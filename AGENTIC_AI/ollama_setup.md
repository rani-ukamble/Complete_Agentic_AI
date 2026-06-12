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


# **********************************

Windows cannot find the **Ollama application** itself:

```text
'ollama' is not recognized as the name of a cmdlet
```

This means one of these happened:

### Option 1: Ollama Desktop App was not installed correctly

Search Windows Start Menu for:

```text
Ollama
```

Do you see an Ollama application?

* Yes → Open it.
* No → Reinstall Ollama.

---

### Option 2: Ollama is installed but not in PATH

Open PowerShell and try:

```powershell
Get-Command ollama -ErrorAction SilentlyContinue
```

If nothing is returned, Windows can't find Ollama.

Now check:

```powershell
dir "$env:LOCALAPPDATA\Programs\Ollama"
```

or

```powershell
dir "C:\Users\$env:USERNAME\AppData\Local\Programs\Ollama"
```

Do you see:

```text
ollama.exe
```

?

---

### Option 3: Run Ollama directly

If you find `ollama.exe`, try:

```powershell
& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" list
```

or

```powershell
& "C:\Users\<your-user>\AppData\Local\Programs\Ollama\ollama.exe" list
```

---

### Option 4: Restart Windows

After installing Ollama, PATH variables are often updated only for new terminals.

Try:

1. Close VS Code completely.
2. Close all PowerShell windows.
3. Reopen VS Code.
4. Open a new terminal.
5. Run:

```bash
ollama --version
```

---

### Quick Diagnostic

In PowerShell run:

```powershell
where.exe ollama
```
# Now check
ollama --version



*****************************

cd D:\AGENTIC_AI_PROJECTS\AGENTIC_AI

python -m venv .venv

.venv\Scripts\activate

pip install ipykernel
python -m ipykernel install --user --name agentic_ai --display-name "Python (agentic_ai)"