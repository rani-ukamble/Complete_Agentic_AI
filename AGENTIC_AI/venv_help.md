

Remove-Item -Recurse -Force .venv

py -3.11 -m venv .venv

.\.venv\Scripts\activate

python --version

pip install ipykernel
python -m ipykernel install --user --name=agentic-ai --display-name "Python 3.11 (agentic-ai)"

# ********************
# ********************

uv python pin cpython-3.11.5-windows-x86_64-none

Remove-Item -Recurse -Force .venv

uv venv --python "C:\Users\Admin\AppData\Local\Programs\Python\Python311\python.exe"


.\.venv\Scripts\activate
python --version

pip install ipykernel
python -m ipykernel install --user --name=agentic-ai --display-name "Python 3.11 (agentic-ai)"

* uv add -r requirements.txt
