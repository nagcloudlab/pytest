


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

Test files should be named test_<something>.py or <something>_test.py.
Test methods and functions should be named test_<something>.
Test classes should be named Test<Something>.

Test Discovery
Pytest will automatically discover tests in files named test_*.py or *_test.py.


Test Outcome

- PASSED(.) - The test ran successfully.
- FAILED(F) - The test failed.
- SKIPPED(s) - The test was skipped.
- XFAI(x) - The test failed, but it was expected to fail.
- XPASS(X) - The test passed, but it was expected to fail.
- ERROR(E) - The test raised an exception.
