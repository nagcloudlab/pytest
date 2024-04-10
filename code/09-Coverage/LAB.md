

Using coverage.py with pytest-cov

```bash
pip install coverage
pip install pytest-cov
```

```bash
cd ..
pytest --cov=cards 09-Coverage
```
- or-

```bash
coverage run --source=cards -m pytest 09-Coverage
coverage report
```

```bash
pytest --cov=cards --cov-report=term-missing 09-Coverage
```



Generating HTML Reports



```bash
pytest --cov=cards --cov-report=html 09-Coverage
```
or

```bash
pytest --cov=cards 09-Coverage
coverage html
```

Running Coverage on Tests

```bash
pytest --cov=cards --cov=09-Coverage 09-Coverage
```


Running Coverage  Directory

```bash
pytest --cov=09-Coverage/some_code 09-Coverage/some_code/test_some_code.py
```

