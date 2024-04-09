# def test_normal():
#     print("\nnormal print")


# def test_fail():
#     print("\nprint in failing test")
#     assert True
#     print("\nline-1")
#     assert False


def hello():
    print("\nhello") # side effect

def test_pass(capsys):
    hello()
    out, err = capsys.readouterr()
    assert out == "\nhello\n"
    assert err == ""


# def test_disabled(capsys):
#     with capsys.disabled():
#         print("\ncapsys disabled print")
