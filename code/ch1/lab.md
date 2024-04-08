




# Installing pytest ( on Linux / Mac )
bash```
python3 -m venv venv
source venv/bin/activate 
pip install pytest
pytest --version
```

# Installing pytest ( on Windows )
bash```
python -m venv venv
venv\Scripts\activate
pip install pytest
pytest --version
```


Running Pytest
===============


bash```

cd code/ch1
pytest test_one.py
pytest -v test_one.py 

pytest test_two.py
pytest -v test_two.py
pytest -vv test_two.py

pytest
pytest --tb=no
pytest --tb=no test_one.py test_two.py
cd ..
pytest --tb=no ch1
pytest ch1/test_one.py::test_passing

```
