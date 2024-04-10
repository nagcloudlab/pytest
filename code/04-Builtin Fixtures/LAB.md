

built-in fixtures
=================


```bash
pytest test_tmp.py
```

Using capsys
------------


```bash
pytest test_version.py
pytest test_print.py
```

capfd—Like capsys, but captures file descriptors 1 and 2, which usually is the same as stdout and stderr
capsysbinary—Where capsys captures text, capsysbinary captures bytes.
capfdbinary—Captures bytes on file descriptors 1 and 2
caplog—Captures output written with the logging package



Using monkeypatch 
-----------------

```bash
pytest test_monkeypatch.py
```


The monkeypatch fixture provides the following functions:

setattr(target, name, value, raising=True)—Sets an attribute
delattr(target, name, raising=True)—Deletes an attribute
setitem(dic, name, value)—Sets a dictionary entry
delitem(dic, name, raising=True)—Deletes a dictionary entry
setenv(name, value, prepend=None)—Sets an environment variable
delenv(name, raising=True)—Deletes an environment variable
syspath_prepend(path)—Prepends path to sys.path, which is Python’s list of import locations
chdir(path)—Changes the current working directory