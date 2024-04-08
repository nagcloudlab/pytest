

Pytest Fixtures
===============

Pytest fixtures are a way to provide data, test doubles, or setup code to tests. 
Fixtures are defined using the `@pytest.fixture` decorator. 
Fixtures can be used by passing the fixture name to a test function. Fixtures can also be used by other fixtures, allowing for fixture composition.

Fixtures can be used to provide data to tests, setup and teardown code, and test doubles.


bash```



display built-in fixtures
pytest --fixtures

cd path/to/code/ch3
pytest -v test_fixtures.py


```


Using Fixtures for Setup and Teardown
=====================================


bash```
cards count
cards add first-item
cards add second-item


bash```
pytest -v test_count_initial.py
```


bash```
pytest -v test_count.py
pytest -v --setup-show test_count.py
```