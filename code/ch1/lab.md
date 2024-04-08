
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
