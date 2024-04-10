


Create a test strategy for the Cards project—the “what tests to write” part of software testing.


-  Selecting and prioritizing which features to test
-  Deciding what to test first
-  Once we know what features need tests, we can generate a list of test cases needed.


Determining Test Scope
---------------------------

- Different projects have different test goals and requirements.

Is security a concern? This is especially important if you save any confidential information.
Performance? Do interactions need to be fast? How fast?
Loading? Can you handle lots of people with lots of requests? Are you expecting to need to? If so, you should test for that.
Input validation? For really any system that accepts input from users, we should validate the data before acting on it.

For cards project:

- Test the behavior of user visible functionality.
- Postpone security, performance, and load testing for the current design. The current design is to have the database stored in the users home directory. When/if that moves to a shared location with multiple users, these concerns will definitely be more important.
- Input validation is also less important while Cards is a single user application. However, I also don’t want stack traces to occur while using the app, so we should test wacky input, at least at the CLI level.


Considering Software Architecture
-----------------------------------


-  The architecture of the software can also influence the test strategy. For example, if you have a monolithic application, you might want to test the entire application at once. If you have a microservices architecture, you might want to test each service individually.

-  For the Cards project, we have a monolithic application. We should test the entire application at once. We can do this by testing the CLI, the database, and the API all together. We can also test the database and API separately, but we should also test them together to ensure they work together correctly.


Evaluating the Features to Test
-----------------------------------

I generally prioritize features to test based on the following factors:

Recent—New features, new areas of code, new functionality that has been recently repaired, refactored, or otherwise modified

Core—Your product’s unique selling propositions (USPs). The essential functions that must continue to work in order for the product to be useful

Risk—Areas of the application that pose more risk, such as areas important to customers but not used regularly by the development team or parts that use third-party code you don’t quite trust

Problematic—Functionality that frequently breaks or often gets defect reports against it

Expertise—Features or algorithms understood by a limited subset of people


```bash
cards --help
```


Core

add, count, delete, finish, list, start, and update all seem like core functionality.
config and version seem less important.
Risk

The third-party packages are Typer for the CLI and TinyDB for the database. Having some focused tests around our use of these components would be prudent. Our use of Typer will be tested when we test the CLI. Our use of TinyDB will be tested really in all of the other tests, and since db.py is isolating our interaction with TinyDB, we can create tests focused at that layer if necessary.



-------------------------------------------------------------------------------------
However, even this quick analysis of features helps us come up with our strategy:

Test core features thoroughly.
Test non-core features with at least one test case.
Test the CLI in isolation.

-------------------------------------------------------------------------------------


Creating Test Cases


-------------------------------------------------------------------------------------

Writing a Test Strategy

Test the behaviors and features that are accessible through the end user interface, the CLI.
Test those features through the API as much as possible.
Test the CLI enough to verify the API is getting properly called for all features.
Test the following core features thoroughly: add, count, delete, finish, list, start, and update.
Include cursory tests for config and version.
Test our use of TinyDB with subsystem tests against db.py.