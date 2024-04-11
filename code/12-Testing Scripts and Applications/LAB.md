

Testing a Simple Python Script

```bash
cd script
python3 hello.py
pytest -v test_hello.py
```

Testing an Importable Python Script

```bash
cd ..
cd script_importable
python3 hello.py
pytest -v test_hello.py
```

Separating Code into src and tests Directories

```bash
cd ..
cd script_src
python3 src/hello.py
pytest -v tests/test_hello.py
```