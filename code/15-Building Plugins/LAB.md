Starting with a Cool Idea
=========================

Behavior            Without plugin          With plugin
----------          -------------           -----------
Exclude slow       pytest -m "not slow"     pytest
Include slow       pytest                   pytest --slow
Only slow          pytest -m slow           pytest -m slow --slow


```bash
cd just_markers
pytest
```

Building a Local conftest Plugin
================================

To modify how pytest works, we need to utilize pytest hook functions

Hook functions are function entry points that pytest provides to allow plugin developers to intercept pytest behavior at certain points and make changes

pytest_configure()—Allows plugins and conftest files to perform initial configuration. We’ll use this hook function to pre-declare the slow marker so users don’t have to add slow to their config files.

pytest_addoption()—Used to register options and settings. We’ll add the --slow flag with this hook.

pytest_collection_modifyitems()—Called after test collection has been performed and can be used to filter or re-order the test items. We need this to find the slow tests, so we can mark them for skipping.

```bash
cd ..
cd local
pytest --help
pytest -v
pytest -v --slow
pytest -v -m "slow" --slow
```

