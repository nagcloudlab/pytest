


```bash
pytest
```


Markers
=======

@pytest.mark.parametrize(argnames, argvalues, indirect, ids, scope): This marker calls a test function multiple times, passing in different arguments in turn.

@pytest.mark.skip(reason=None): This marker skips the test with an optional reason.
@pytest.mark.skipif(condition, ..., *, reason): This marker skips the test if any of the conditions are True.
@pytest.mark.xfail(condition, ..., *, reason, run=True, raises=None, strict=xfail_strict): This marker tells pytest that we expect the test to fail.
@pytest.mark.usefixtures(fixturename1, fixturename2, ...): This marker marks tests as needing all the specified fixtures.

These are the most commonly used of these builtins:

@pytest.mark.parametrize()
@pytest.mark.skip()
@pytest.mark.skipif()
@pytest.mark.xfail()


Skipping Tests with pytest.mark.skip
====================================

```bash
cd builtins
pytest --tb=no test_less_than.py
pytest --tb=no test_skip.py
pytest --tb=no -ra test_skip.py
```


Skipping Tests Conditionally with pytest.mark.skipif
====================================================

```bash
pytest --tb=no test_skipif.py
pytest --tb=no -ra test_skipif.py
```


Expecting Tests to Fail with pytest.mark.xfail
==============================================

```bash
pytest --tb=no -ra test_xfail.py
```

For tests marked with xfail:

Failing tests will result in XFAIL.
Passing tests (with no strict setting) will result in XPASSED.
Passing tests with strict=true will result in FAILED.

When a test fails that is marked with xfail, pytest knows exactly what to tell you: “You were right, it did fail,” which is what it’s saying with XFAIL. 

For tests marked with xfail that actually pass, pytest is not quite sure what to tell you. It could result in XPASSED, which roughly means, “Good news, the test you thought would fail just passed.” Or it could result in FAILED, or, “You thought it would fail, but it didn’t. You were wrong.”


Selecting Tests with Custom Markers
===================================

```bash
cd ..
cd smoke
pytest --tb=no test_start_unmarked.py
pytest --tb=no -m "smoke" test_start.py

pytest --tb=no -vs -m "exception" test_start.py
```

Marking Files, Classes, and Parameters
======================================

```bash
cd ..
cd multiple
pytest --tb=no
pytest --tb=no -m "exception"
pytest --tb=no -m "smoke"
pytest --tb=no -m "finish"
```


Using “and,” “or,” “not,” and Parentheses with Markers
=====================================================

```bash
pytest -v -m "finish and exception"
pytest -v -m "finish and not smoke"
pytest -v -m "(exception or smoke) and not finish"
pytest -v -m "(exception or smoke) and not finish"
pytest -v -m smoke -k "not TestFinish"
```


Being Strict with Markers
=========================

```bash
cd ..
cd bad
pytest -m smoke


Combining Markers with Fixtures
===============================

```bash
cd ..
cd combined
pytest -v -s --setup-show test_num_cards.py


Listing Markers
===============

```bash
cd ..
cd multiple
pytest --markers
```
