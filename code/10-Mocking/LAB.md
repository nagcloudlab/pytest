

the mock package is used to swap out pieces of the system to isolate bits of our application code from the rest of the system. 

Mock objects are sometimes called test doubles, spies, fakes, or stubs.

pytest’s own monkeypatch fixture and mock, you should have all the test double functionality you need.




Isolating the Command-Line Interface
====================================


The Cards CLI uses the Typer library to handle all of the command-line parts, and then it passes the real logic off to the Cards API.

n testing the Cards CLI, the idea is that we’d like to test the code within cli.py and cut off access to the rest of the system. To do that, we have to look at cli.py to see how it’s accessing the rest of Cards.

cards_proj/src/cards/cli.py

Through this cards namespace, cli.py accesses:

cards.__version__ (a string)
cards.CardDB (a class representing the main API methods)
cards.InvalidCardID (an exception)
cards.Card (the primary data type for use between the CLI and API)


Testing with Typer
==================

Typer is a library that makes it easy to build command-line interfaces in Python. It’s built on top of Click, which is another popular CLI library.

```bash
pytest -v -s test_typer_testing.py::test_typer_runner
pytest -v -s test_typer_testing.py::test_cards_cli
```


Mocking a Class and Methods
=========================

```bash
pytest -v -s test_mock.py::test_mock_version
pytest -v -s test_mock.py::test_version
```

```bash
pytest -v -s test_mock.py::test_mock_CardsDB
```


```bash
pytest -v -s test_mock.py::test_mock_path
```


Using Plugins to Assist Mocking

There are many plugins that help with mocking, such as pytest-mock, which is a general-purpose plugin that provides a mocker fixture that acts as a thin wrapper around unittest.mock. One benefit of using pytest-mock is that the fixture cleans up after itself, so you don’t have to use a with block, as we did in our examples.

There are also several special-purpose mocking libraries that should be considered if their focus matches what you are testing:

For mocking database access, try pytest-postgresql, pytest-mongo, pytest-mysql, and pytest-dynamodb.

For mocking HTTP servers, try pytest-httpserver.

For mocking requests, try responses and betamax.

And there are even more tools, such as pytest-rabbitmq, pytest-solr, pytest-elasticsearch, and pytest-redis.