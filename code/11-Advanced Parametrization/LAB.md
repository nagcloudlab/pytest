

Using Complex Values
--------------------

```bash
pytest -v -s test_ids.py::test_finish
pytest -v -s test_ids.py::test_card
```

Creating Custom Identifiers
---------------------------

```bash
pytest -v -s test_ids.py::test_id_str
```

Writing Custom ID Functions
---------------------------

```bash
pytest -v -s test_ids.py::test_id_func
pytest -v -s test_ids.py::test_id_lambda
```

Adding an ID to pytest.param
---------------------------

```bash
pytest -v -s test_ids.py::test_id_param
```

Using an ID List
----------------

```bash
pytest -v -s test_ids.py::test_id_list
```


Parametrizing with Dynamic Values
---------------------------------

```bash
pytest -v -s test_param_gen.py
```

Using Multiple Parameters
-------------------------

```bash
pytest -v -s test_multiple.py::test_add_lots
pytest -v -s test_multiple.py::test_stacking
```

Using Indirect Parametrization
------------------------------

```bash

pytest -v -s test_indirect.py