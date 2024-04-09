


Testing Without Parametrize
============================


bash```
pytest -v test_finish.py
pytest -v test_finish_combined.py
```

It passes, and we have eliminated the redundant code. Woohoo! But, there are other problems:

We have one test case reported instead of three.
If one of the test cases fails, we really don’t know which one without looking at the traceback or some other debugging information.
If one of the test cases fails, the test cases following the failure will not be run. pytest stops running a test when an assert fails.

Solution: Parametrize


Parametrizing Functions
========================

bash```
pytest -v test_func_param.py::test_finish
```

Parametrizing Fixtures
======================

bash```
pytest -v test_fix_param.py::test_finish
```


Parametrizing with pytest_generate_tests hook
============================================

bash```
pytest -v test_gen.py::test_finish
```


Using Keywords to Select Test Cases
===================================


bash```
pytest -v 
pytest -v -k todo
pytest -v -k "todo and not (play or create)"
pytest -v "test_func_param.py::test_finish"
pytest -v "test_func_param.py::test_finish[a-b]"
```

