# Incubyte TDD — String Calculator (Python + pytest)


This repository contains a TDD-first implementation of the *String Calculator* kata (Incubyte assessment).


## Implemented behavior
- `add("")` returns `0`
- Single number returns its value
- Two numbers (comma separated) sum correctly
- Any amount of numbers supported
- Newlines accepted as separators (e.g. `"1\n2,3"`)
- Custom delimiter supported using the `//[delimiter]\n[numbers]` format (e.g. `//;\n1;2`)
- Negative numbers raise an exception listing all negatives (e.g. `negatives not allowed: -4,-5`)


> Optional/extension rules are commented or left as hints in the code so you can complete them for extra points (ignore >1000, multi-char/multiple delimiters).


## Quick start
```bash
python -m venv .venv
source .venv/bin/activate # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q