


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

bash```
cd code/ch6/builtins
pytest --tb=no test_less_than.py
pytest --tb=no test_skip.py
pytest --tb=no -ra test_skip.py
```


Skipping Tests Conditionally with pytest.mark.skipif
====================================================

bash```
pytest --tb=no test_skipif.py
pytest --tb=no -ra test_skipif.py
```