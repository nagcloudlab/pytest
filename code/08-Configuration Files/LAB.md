

```bash
pytest --help
```


Understanding pytest Configuration Files


Let’s run down the non-test files relevant to pytest:

pytest.ini: 
    This is the primary pytest configuration file that allows you to change pytest’s default behavior.
    Its location also defines the pytest root directory, or rootdir.

conftest.py: 
    This file contains fixtures and hook functions. 
    It can exist at the rootdir or in any subdirectory.    

__init__.py: 
    When put into test subdirectories, 
    this file allows you to have identical test file names in multiple test directories.


tox.ini, pyproject.toml, and setup.cfg: 
    These files can take the place of pytest.ini. 
    If you already have one of these files in a project, you can use it to save pytest settings.

    tox.ini is used by tox, the command-line automated testing tool
    pyproject.toml is used for packaging Python projects and can be used to save settings for various tools, including pytest.
    setup.cfg is also used for packaging, and can be used to save pytest settings.

https://nagcloudlab.notion.site/PyTest-b8d4930fe73b40749acab0b8f79b5d06?pvs=4


Saving Settings and Flags in pytest.ini

Using tox.ini, pyproject.toml, or setup.cfg in place of pytest.ini


Determining a Root Directory and Config File


- Even before it starts looking for test files to run, pytest reads the configuration file—the pytest.ini file or the tox.ini, setup.cfg, or pyproject.toml files that contain a pytest section.


- If you’ve passed in a test directory, pytest starts looking there.

```bash
pytest dir1
```

- If you’ve passed in multiple files or directories, pytest starts at the common ancestor of all of them


```bash
pytest dir1 dir2 file1.py file2.py
```

- If you don’t pass in a file or directory, it starts at the current directory. 

```bash
pytest
```

-  If pytest finds a configuration file at the starting directory, that’s the root. 

- If not, pytest goes up the directory tree until it finds a configuration file that has a pytest section in it.

- Once pytest finds a configuration file, it marks the directory where it found it as the root directory, or rootdir. 

- This root directory is also the relative root of test node IDs. It also tells you where it found a configuration file.


---------------


- Sharing Local Fixtures and Hook Functions with conftest.py

----------------


Avoiding Test File Name Collision with __init__.py
https://nagcloudlab.notion.site/PyTest-b8d4930fe73b40749acab0b8f79b5d06?pvs=4


```bash
cd ..
cd dup
tree tests_with_init
pytest tests_with_init -v
tree tests_no_init
pytest tests_no_init -v
```