python -m venv venv

venv\Scripts\activate      # On Windows

pip install -r requirements.txt


set PYTHONPATH=%CD%\src
pytest -v