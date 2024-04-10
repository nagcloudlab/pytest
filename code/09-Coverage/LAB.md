

Using coverage.py with pytest-cov

```bash
pip install coverage
pip install pytest-cov
```

```bash
cd ..
pytest --cov=cards --cov=foo --cov 07-Strategy
```
- or-

```bash
coverage run --source=cards -m pytest 07-Strategy
coverage report
```

```bash
pytest --cov=cards --cov-report=term-missing 07-Strategy
```


Generating HTML Reports


```bash
pytest --cov=cards --cov-report=html 07-Strategy
```
or

```bash
pytest --cov=cards 07-Strategy
coverage html
```


Running Coverage on Tests

```bash
pytest --cov=cards --cov=09-Coverage --cov-report=html 09-Coverage
```


Running Coverage  Directory

```bash
pytest --cov=09-Coverage/some_code 09-Coverage/some_code/test_some_code.py
```


Running Coverage on a Single File

```bash
pytest --cov=single_file single_file.py
```