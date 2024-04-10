import pytest
from cards import Card
import sys

import cards
from packaging.version import parse


@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="Card < comparison not supported in 1.x",
)
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2


def test_fn1():
    assert True

@pytest.mark.skipif(
    not sys.platform.startswith("win"),    
    reason="Test not supported on Windows",
)
def test_fn2():
    assert True



# pytest.skip
def test_tracers_as_arrays_manual():
    try:
        import numpy
    except ImportError:
        pytest.skip("requires numpy")


# pytest.importorskip        
def test_tracers_as_arrays():
    numpy = pytest.importorskip("numpy")
    ...
