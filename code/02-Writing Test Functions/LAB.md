

Writing Test Functions
=======================

install cards_proj package

```bash
cd code
pip install ../00-cards_proj/

cards
cards add do something --owner Nag
cards add do something else
cards
cards update 2 --owner Nag

cards start 1
cards finish 1
cards start 2
cards delete 1
cards

```

Using Test Functions
====================


```bash
pytest test_card.py
```


Using assert Statements
========================

assert something
assert not something
asert a==b
assert a!=b
assert a is None
assert a is not None
assert a <= b


```bash
pytest test_card_fail.py
pytest -vv test_card_fail.py
```


Failing with pytest.fail() and Exceptions
=========================================

A test will fail if there is any uncaught exception. This can happen if

an assert statement fails, which will raise an AssertionError exception,
the test code calls pytest.fail(), which will raise an exception, or
any other exception is raised.

While any exception can fail a test, I prefer to use assert. In rare cases where assert is not suitable, use pytest.fail().


```bash
pytest test_alt_fail.py
pytest -vv test_alt_fail.py
```

When calling pytest.fail() or raising an exception directly, we don’t get the wonderful assert rewriting provided by pytest. 
However, there are reasonable times to use pytest.fail(), such as in an assertion helper.


Writing Assertion Helper Functions
==================================

```bash
pytest test_helper.py
pytest -vv test_helper.py
```


Testing for Expected Exceptions
================================

pytest.raises() is a context manager that returns an exception object. We can use this object to check the exception type and message.


```bash
pytest test_experiment.py
```

```bash
pytest test_exceptions.py
```


Structuring Test Functions
==========================

Arrange,Act,Assert (AAA) pattern
or
Given, When, Then pattern


Given/Arrange—A starting state. This is where you set up data or the environment to get ready for the action.

When/Act—Some action is performed. This is the focus of the test—the behavior we are trying to make sure is working right.

Then/Assert—Some expected result or end state should happen. At the end of the test, we make sure the action resulted in the expected behavior.



Grouping Tests with Classes
===========================

```bash
pytest test_classes.py::TestEquality
pytest test_classes.py::TestEquality::test_equality
```


Running a Subset of Tests
=========================

single test method

```bash
pytest path/to/test_file.py::TestClass::test_method
```

All tests in a class

```bash
pytest path/to/test_file.py::TestClass
```

Single test function

```bash
pytest path/to/test_file.py::test_function
```

All tests in a file

```bash
pytest path/to/test_file.py
```

All tests in a directory

```bash
pytest path/to/directory
```

All tests in a directory with a pattern

```bash
pytest path/to/directory -k pattern
```


```bash
cd /path/to/code
```

Running a single test method, test class, or module:

```bash
pytest test_classes.py::TestEquality::test_equality
pytest test_classes.py::TestEquality
pytest test_classes.py
```

Running a single test function or module:

```bash
pytest test_classes.py::test_defaults
pytest test_card.py
```

Running all tests in a directory:

```bash
pytest <dir>

pytest -v -k TestEquality
pytest -v -k TestEq
pytest -v --tb=no -k equality
pytest -v --tb=no -k "equality and not equality_fail"
pytest -v --tb=no -k "(dict or ids) and not TestEquality"

```
