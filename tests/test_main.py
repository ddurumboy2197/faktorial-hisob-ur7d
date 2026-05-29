import pytest

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

def test_faktorial():
    assert faktorial(0) == 1
    assert faktorial(1) == 1
    assert faktorial(2) == 2
    assert faktorial(3) == 6
    assert faktorial(4) == 24
    assert faktorial(5) == 120

def test_faktorial_negative():
    with pytest.raises RecursionError:
        faktorial(-1)

def test_faktorial_float():
    with pytest.raises TypeError:
        faktorial(3.5)
