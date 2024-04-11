

Adding a New Feature to the Cards Project


```bash
cards list
cards list --help
cards list --state done
```


Installing Cards in Editable Mode

```bash
​​python3​​ ​​-m​​ ​​venv​​ ​​venv
source venv/bin/activate
pip install -U pip

pip install -e "./cards_proj/[test]"

cd cards_proj
pytest --tb=no

```

pytest includes quite a few command-line flags that are useful for debugging. We will be using some of these to debug our test failures.

Flags for selecting which tests to run, in which order, and when to stop:

-lf / --last-failed: Runs just the tests that failed last

-ff / --failed-first: Runs all the tests, starting with the last failed

-x / --exitfirst: Stops the tests session after the first failure

--maxfail=num: Stops the tests after num failures

-nf / --new-first: Runs all the tests, ordered by file modification time

--sw / --stepwise: Stops the tests at the first failure. Starts the tests at the last failure next time

--sw-skip / --stepwise-skip: Same as --sw, but skips the first failure



Flags to control pytest output:

-v / --verbose: Displays all the test names, passing or failing
--tb=[auto/long/short/line/native/no]: Controls the traceback style
-l / --showlocals: Displays local variables alongside the stacktrace


Flags to start a command-line debugger:

--pdb: Starts an interactive debugging session at the point of failure

--trace: Starts the pdb source-code debugger immediately when running each test

--pdbcls: Uses alternatives to pdb, such as IPython’s debugger with --pdbcls=IPython.terminal.debugger:TerminalPdb

For all of these descriptions, “failure” refers to a failed assertion or any other uncaught exception found in our source code or test code, including fixtures.


Re-Running Failed Tests

```bash
pytest --lf --tb=no
pytest --lf -x --tb=no
pytest --lf -x -l --tb=short
```


Debugging with pdb


You can launch pdb from pytest in a few different ways:

Add a breakpoint() call to either test code or application code. When a pytest run hits a breakpoint() function call, it will stop there and launch pdb.

Use the --pdb flag. With --pdb, pytest will stop at the point of failure. In our case, that will be at the assert len(the_list) == 2 line.

Use the --trace flag. With --trace, pytest will stop at the beginning of each test.

```bash
pytest --lf --trace
```

Meta commands:

h(elp): Prints a list of commands
h(elp) command: Prints help on a command
q(uit): Exits pdb
Seeing where you are:

l(ist) : Lists 11 lines around the current line. Using it again lists the next 11 lines, and so on.

l(ist) .: The same as above, but with a dot. Lists 11 lines around the current line. Handy if you’ve use l(list) a few times and have lost your current position

l(ist) first, last: Lists a specific set of lines

ll : Lists all source code for the current function

w(here): Prints the stack trace

Looking at values:

p(rint) expr: Evaluates expr and prints the value

pp expr: Same as p(rint) expr but uses pretty-print from the pprint module. Great for structures

a(rgs): Prints the argument list of the current function

Execution commands:

s(tep): Executes the current line and steps to the next line in your source code even if it’s inside a function

n(ext): Executes the current line and steps to the next line in the current function

r(eturn): Continues until the current function returns

c(ontinue): Continues until the next breakpoint. When used with --trace, continues until the start of the next test

unt(il) lineno: Continues until the given line number

```bash
ll
until 8
step
ll
return
pp done_cards
step
pp the_list
exit
```

```bash
pytest --lf -x -v --tb=no
```