

Create Virtual Environment & Install pytest
===========================================

on linux / mac

```bash
python3 -m venv venv
source venv/bin/activate 
pip install pytest
pytest --version
```

on windows

```bash
python -m venv venv
venv\Scripts\activate
pip install pytest
pytest --version
```


Running Pytest
===============

```bash

pytest
pytest test_one.py
pytest -v test_one.py 
pytest test_two.py
pytest -v test_two.py
pytest -vv test_two.py
pytest --tb=no test_one.py test_two.py
pytest test_one.py::test_passing
pytest --tb=no
pytest --tb=no <dir>


```
