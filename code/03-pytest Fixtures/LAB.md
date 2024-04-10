

```bash
pytest -v --setup-show test_fixtures.py
```

Using Fixtures for Setup and Teardown
=====================================

```bash
pytest  --setup-show test_count_initial.py
```

```bash
pytest  --setup-show -v test_count.py
```

Specifying Fixture Scope
========================

scope='function' => Run once per test function
scope='class' => Run once per test class
scope='module' => Run once per test module
scope="package" => Run once per test package
scope="session" => Run once per test session



```bash
pytest  --setup-show -v test_mod_scope.py
```



```bash
cd a
pytest  --setup-show -v test_count.py
pytest --setup-show -v 
```

Using Multiple Fixture Levels
=============================

```bash
cd ..
cd b
pytest --setup-show -v 
```


Finding Where Fixtures Are Defined
==================================

```bash
pytest --fixtures 
```

You can also use --fixtures-per-test to see what fixtures are used by each test and where the fixtures are defined:

```bash
pytest --fixtures-per-test test_count.py::test_empty
```


Using Multiple Fixtures per Test or Fixture
===========================================


```bash
cd ..
cd c
pytest --setup-show -v 
```


Deciding Fixture Scope Dynamically
==================================

```bash
cd ..
cd d
pytest --setup-show -v test_count.py
pytest --setup-show --func-db -v test_count.py
```


Using autouse for Fixtures That Always Get Used
===============================================


```bash
cd ..
pytest --setup-show -v test_autouse.py

pytest --setup-show -v --capture=no test_autouse.py
or
pytest --setup-show -v -s test_autouse.py


Renaming Fixtures
=================

```bash
pytest --setup-show -v test_rename_fixture.py
```