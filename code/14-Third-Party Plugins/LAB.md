

As powerful as pytest is right out of the box, it gets even better when we add plugins to the mix.


The pytest code base is designed to allow customization and extensions, and there are hooks available to allow modifications and improvements through plugins.

Any time you put fixtures and/or hook functions into a project’s conftest.py file, you create a local plugin.


It’s just a little bit of extra work to convert these conftest.py files into installable plugins that you can share between projects, with other people, or with the world.


You can find third-party pytest plugins in several places.

https://docs.pytest.org/en/latest/reference/plugin_list.html
https://pypi.org
https://github.com/pytest-dev
https://docs.pytest.org/en/latest/how-to/plugins.html


Installing Plugins
==================

```bash
​​pip​​ ​​install​​ ​​pytest-cov
```

This command installs the pytest-cov plugin, which adds code coverage reporting to pytest.




Exploring the Diversity of pytest Plugins
=========================================



1. Plugins That Change the Normal Test Run Flow

    - pytest, by default, runs our tests in a predictable flow.
    - Given a single directory of test files, pytest will run each file in alphabetical order. 
    - Within each file, each test is run in the order it appears in the file.

    Sometimes it’s nice to change that order. The following plugins in some way change the normal test run flow:

    > pytest-order—Allows us to specify the order using a marker

    > pytest-randomly—Randomizes the order, first by file, then by class, then by test

    > pytest-repeat—Makes it easy to repeat a single test, or multiple tests, a specific number of times

    > pytest-rerunfailures—Re-runs failed tests. Helpful for flaky tests

    > pytest-xdist—Runs tests in parallel, either using multiple CPUs on one machine, or multiple remote machines

    ... and many more


2. Plugins That Alter or Enhance Output

    The normal pytest output shows mostly dots for passing tests, and characters for other output. Then you’ll see lists of test names with outcome if you pass in -v. However, there are plugins that change the output.

    > pytest-html—Generates an HTML report of the test results

    > pytest-metadata—Adds metadata to the test results, such as the Python version, platform, and packages installed

    > pytest-sugar—Changes the output to be more colorful and easier to read

    > pytest-testrail—Integrates with TestRail, a test case management tool

    > pytest-watch—Automatically re-runs tests when files change

    > pytest-instafail—Shows failures and errors instantly, rather than waiting until the end of the test run

    > pytest-emoji—Changes the output to use emojis

    > pytest-verbose-parametrize—Shows the parameters used in parametrized tests

    > pytest-excel—Generates an Excel report of the test results


3. Plugins for Web Development

    If you’re working on a web project, there are plugins that can help you test your web application.

    > pytest-django—Adds fixtures and other helpers for testing Django applications

    > pytest-flask—Adds fixtures and other helpers for testing Flask applications

    > pytest-splinter—Adds fixtures for Splinter, a tool for web application testing

    > pytest-selenium—Adds fixtures for Selenium, a tool for web application testing

    > pytest-bdd—Adds support for behavior-driven development (BDD) using Gherkin syntax

    > pytest-cov—Adds code coverage reporting

    > pytest-mock—Adds fixtures for mocking


4. Plugins for Fake Data

    Sometimes you need fake data for your tests. There are plugins that can help with that.

    > Faker—Generates fake data for you. Provides faker fixture for use with pytest

    > model-bakery—Generates Django model objects with fake data.

    > pytest-factoryboy—Includes fixtures for Factory Boy, a database model data generator

    > pytest-mimesis—Generates fake data similar to Faker, but Mimesis is quite a bit faster


5. Plugins That Extend pytest Functionality

    All plugins extend pytest functionality, but I was running out of good category names. This is a grab bag of various cool plugins.

    > pytest-cov—Runs coverage while testing

    > pytest-benchmark—Runs benchmark timing on code within tests

    > pytest-timeout—Doesn’t let tests run too long

    > pytest-asyncio—Tests async functions

    > pytest-bdd—Writes behavior-driven development (BDD)–style tests with pytest

    > pytest-freezegun—Freezes time so that any code that reads the time will get the same value during a test. You can also set a particular date or time.

    > pytest-mock—A thin-wrapper around the unittest.mock patching API



6. Plugins for Big Data

    If you’re working with big data, there are plugins that can help you test your big data applications.

    > pytest-spark—Adds fixtures for testing PySpark applications

    > pytest-hadoop—Adds fixtures for testing Hadoop applications

    > pytest-hive—Adds fixtures for testing Hive applications

    > pytest-hbase—Adds fixtures for testing HBase applications

    > pytest-impala—Adds fixtures for testing Impala applications

    > pytest-aws—Adds fixtures for testing AWS applications

    > pytest-azure—Adds fixtures for testing Azure applications

    > pytest-gcp—Adds fixtures for testing Google Cloud Platform applications

    > pytest-kafka—Adds fixtures for testing Kafka applications

    > pytest-cassandra—Adds fixtures for testing Cassandra applications

    > pytest-mongo—Adds fixtures for testing MongoDB applications

    > pytest-sql—Adds fixtures for testing SQL applications

    > pytest-redis—Adds fixtures for testing Redis applications

    <!-- ... and many more -->
    



Running Tests in Parallel
==========================

```bash
pytest test_parallel.py
pip install pytest-repeat
pytest test_parallel.py --count=10
pip install pytest-xdist
pytest test_parallel.py -n=10
pytest test_parallel.py -n=auto --count=32
```


Randomizing Test Order
=======================

```bash
cd ..
cd random
pytest -v
pip install pytest-randomly
pytest -v