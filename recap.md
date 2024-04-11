

Installing pytest

```bash
pip install pytest
```


Writing tests

```python
def test_example():
    assert 1 + 1 == 2
```

Running tests

```bash
pytest
```


Assertions
    
```python
# Check that two values are equal
assert foo() == 4

# Check that a value is True
assert foo()
# Check that a value is False
assert not foo()
# Check that a value is None
assert foo() is None
# Check that a value is not None
assert foo() is not None
# Check that a value is in a list
assert 1 in [1, 2, 3]
# Check that a value is not in a list
assert 4 not in [1, 2, 3]
# Check that a value is in a dictionary
assert 'key' in {'key': 'value'}
# Check that a value is not in a dictionary
assert 'key' not in {'key': 'value'}
# Check that two values are the same object
assert foo() is bar()
# Check that two values are not the same object
assert foo() is not bar()
# Check that two values are almost equal
assert math.isclose(0.1 + 0.2, 0.3)
```

Fixtures

```python
@pytest.fixture
def int_list():
    return [1, 2, 3]

def test_sum(int_list):
    assert sum(int_list) == 6
```

```python
@pytest.fixture
def custom_list(length):
    return [1] * length

def test_custom_list(custom_list):
    assert len(custom_list) == 3

@pytest.fixture(scope='module')
def fixture_with_module_scope():
    return 'module-scoped fixture'

```


Parametrizing tests

```python
@pytest.mark.parametrize('x,y', [(1, 2), (2, 3), (3, 4)])
def test_addition(x, y):
    assert x + y == x + y

@pytest.fixture(params=[1, 2, 3])
def fixture_with_params(request):
    return request.param

def test_fixture_with_params(fixture_with_params):
    assert fixture_with_params in [1, 2, 3]
```

Markers

```python
@pytest.mark.slow
def test_long_running_function():
    # Test code here

@pytest.mark.slow
@pytest.mark.important
def test_critical_function():
    # Test code here
```

```bash
pytest -m slow
pytest -m slow and not important
pytest -k foo
```

skip

```python
@pytest.mark.skip
def test_function_that_is_not_implemented_yet():
    pass

@pytest.mark.skip('This test is not relevant for this environment')
def test_environment_specific_function():
    pass
```

xfail

```python
@pytest.mark.xfail
def test_function_that_is_known_to_fail():
    assert foo() == 4

@pytest.mark.xfail('sys.platform == "windows"')
def test_function_that_fails_on_windows():
    assert foo() == 4
```

xfail_strict

```python
@pytest.mark.xfail_strict
def test_function_that_is_known_to_fail_strictly():
    assert foo() == 4

@pytest.mark.xfail_strict('sys.platform == "windows"')
def test_function_that_fails_on_windows_strictly():
    assert foo() == 4
```


skipif

```python
@pytest.mark.skipif('sys.platform == "windows"')
def test_function_that_is_not_relevant_on_windows():
    pass
```

usefixtures

```python
@pytest.mark.usefixtures('fixture1', 'fixture2')
def test_function_with_fixtures(fixture1, fixture2):
    # Test code here
```


raises


```python
@pytest.mark.raises(ValueError)
def test_function_that_raises_value_error():
    raise ValueError('This is a test')

@pytest.mark.raises(ValueError, 'Invalid value')
def test_function_that_raises_value_error():
    raise ValueError('Invalid value')
```



File structure in a typical python project

my_project/
├── pytest.ini
├── conftest.py
├── tests/
│   ├── test_module1.py
│   ├── test_module2.py
│   ├── subdir1/
│   │   ├── conftest.py
│   │   ├── test_submodule1.py
│   ├── subdir2/
│   │   ├── conftest.py
│   │   ├── test_submodule2.py
│   └── data/
│       ├── test_data.txt
└── src/
    ├── module1.py
    └── module2.py


pytest.ini

```ini
[pytest]

; Specifying test file patterns
testpaths = tests
norecursedirs = .git .tox .env .venv venv

python_files = test_*.py *_test.py 
python_classes = Test*
python_functions = test_*


addopts = --strict --verbose --color=yes --cov=src --cov-report=term-missing

; enable / disable plugins
plugins = pytest-cov pytest-xdist pytest-repeat


; set environmental variables
env =
    ENVIRONMENT=test
    DATABASE_URL=sqlite:///:memory:

; set markers
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    important: marks tests as important
    xfail: marks tests as expected to fail
    skip: marks tests as skipped
    raises: marks tests as expecting an exception

; set filterwarnings
filterwarnings =
    ignore::DeprecationWarning
    ignore::PendingDeprecationWarning
    ignore::UserWarning
    ignore::ResourceWarning
    ignore::RuntimeWarning
    ignore::ImportWarning
    ignore::FutureWarning
    ignore::Warning
  
```


conftest.py

```python

import pytest

@pytest.fixture
def my_fixture():
    return 'fixture value'

def pytest_addoption(parser):
    parser.addoption('--myopt', action='store', default='default',
                     help='my option: type=str')

def pytest_configure(config):
    config.addinivalue_line('markers', 'important: mark test as important')

def pytest_collection_modifyitems(config, items):
    for item in items:
        if 'important' in item.keywords:
            item.add_marker(pytest.mark.slow)

def pytest_generate_tests(metafunc):
    if 'param' in metafunc.fixturenames:
        metafunc.parametrize('param', [1, 2, 3])

def pytest_runtest_setup(item):
    if 'important' in item.keywords and item.config.getoption('myopt') == 'default':
        pytest.skip('test requires --myopt option to run')

def pytest_runtest_teardown(item, nextitem):
    if 'important' in item.keywords and item.config.getoption('myopt') == 'default':
        print('cleaning up after important test')

def pytest_runtest_call(item):
    if 'important' in item.keywords and item.config.getoption('myopt') == 'default':
        print('running important test')

def pytest_runtest_makereport(item, call):
    if 'important' in item.keywords and item.config.getoption('myopt') == 'default':
        print('reporting important test')

def pytest_terminal_summary(terminalreporter):
    if terminalreporter.config.getoption('myopt') == 'default':
        print('terminal summary')

def pytest_add_marker(name, mark):
    if name == 'custom':
        return pytest.mark.Marker(name)

    def pytest_add_marker(name, mark):
    if name == 'custom':
        return pytest.mark.Marker(name, args=['arg1', 'arg2']

```

test_module1.py

```python
@pytest.mark.custom('arg1', 'arg2')
def test_module1():
    assert 1 + 1 == 2
```



Implementing custom test discovery mechanisms

conftest.py

```python
import pytest

def pytest_collect_file(path, parent):
    if path.ext == '.txt':
        return TextFileTests(path, parent)

class TextFileTests(pytest.File):
    def collect(self):
        with self.fspath.open('r') as f:
            for line in f:
                if line.startswith('test_'):
                    name = line.strip()
                    yield TestFunction(name, self)
class TestFunction(pytest.Item):
    def runtest(self):
        # Test code here
        pass
```


Sharing fixtures across test modules

conftest.py

```python
import pytest

@pytest.fixture
def my_fixture():
    return 'fixture value'
```

Customizing the scope of fixtures

Customizing the behavior of fixtures

conftest.py

```python
import pytest

import pytest

@pytest.fixture(autouse=True)
def fixture_c():
    print('setup fixture_c')
    yield
    print('teardown fixture_c')

```

Test Report Generation

```bash
pip install pytest-html
```

```bash
pytest --html=report.html
pytest --html=report.html --self-contained-html
```



Mocking

```bash
pip install pytest-mock
```

```python
import pytest
import requests
from unittest.mock import Mock

@pytest.fixture
def mock_get(mocker):
    mock = Mock()
    mocker.patch('requests.get', return_value=mock)
    return mock
def test_get_request(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'key': 'value'}
    response = requests.get('http://example.com')
    assert response.status_code == 200
    assert response.json() == {'key': 'value'}
```

Mocking properties

```python
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_obj(mocker):
    mock = Mock()
    mock.some_property.side_effect = ['a', 'b', 'c']
    return mock
def test_mock_property(mock_obj):
    assert mock_obj.some_property == 'a'
    assert mock_obj.some_property == 'b'
    assert mock_obj.some_property == 'c'

```

Mocking methods

```python
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_obj(mocker):
    mock = Mock()
    mock.some_method.return_value = 'mocked value'
    return mock
def test_mock_method(mock_obj):
    assert mock_obj.some_method() == 'mocked value'

```


Mocking context managers

```python
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_obj(mocker):
    mock = Mock()
    mock.__enter__.return_value = 'mocked value'
    return mock
def test_mock_context_manager(mock_obj):
    with mock_obj as value:
        assert value == 'mocked value'
```


Mocking snowflake connections

```python
import snowflake.connector
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_snowflake(mocker):
    mock_conn = Mock(spec=snowflake.connector.connect)
    mocker.patch('snowflake.connector.connect', return_value=mock_conn)
    return mock_conn

def test_read_snowflake_table(mock_snowflake):
    mock_cursor = Mock()
    
    mock_cursor.execute.return_value = [['column1', 'column2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']]
    mock_snowflake.cursor.return_value = mock_cursor
    # Test code that reads a Snowflake table
    # ...
    mock_cursor.execute.assert_called_once()
    mock_cursor.execute.assert_called_with('SELECT * FROM table')
    assert mock_cursor.execute.call_count == 1
    assert mock_cursor.execute.call_args == (('SELECT * FROM table',),)
    assert mock_cursor.execute.call_args_list == [(('SELECT * FROM table',),)]
    assert mock_cursor.execute.call_args_list[0][0] == ('SELECT * FROM table',)
    assert mock_cursor.execute.call_args_list[0][1] == {}

```
