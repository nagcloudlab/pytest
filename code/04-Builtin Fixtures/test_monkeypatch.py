
import getpass

import pytest



class AuthenticationError(RuntimeError):
    pass


def check_credentials(name, password):
    if password == "wrong-pass":
        raise AuthenticationError("wrong password")
    return True

def user_login(name):
    password = getpass.getpass() # prompt for passwords
    check_credentials(name, password)
    ...
    return True

# --------------------------------------------------

def test_login_success(monkeypatch):
    monkeypatch.setattr(getpass, "getpass",lambda: "correct-pass")
    assert user_login("joe")


def test_login_failure(monkeypatch):
    monkeypatch.setattr(getpass, "getpass", lambda: "wrong-pass")
    with pytest.raises(AuthenticationError,match="wrong password"):
        user_login("joe")

# --------------------------------------------------