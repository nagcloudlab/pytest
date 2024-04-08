

Writing Test Functions
=======================


Application Code ( cards_proj )
-------------------------------


install cards_proj package

bash```
cd code
pip install ./cards_proj/

cards
cards add dome something --owner Nag
cards add dome something else
cards
cards update 2 --owner Nag

cards start 1
cards finish 1
cards start 2
cards delete 1
cards

```


bash```
cd /path/to/code/ch2
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


bash```
cd /path/to/code/ch2
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


bash```
cd /path/to/code/ch2
pytest test_alt_fail.py
pytest -vv test_alt_fail.py
```


When calling pytest.fail() or raising an exception directly, we don’t get the wonderful assert rewriting provided by pytest. 

However, there are reasonable times to use pytest.fail(), such as in an assertion helper.