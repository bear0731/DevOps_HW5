# test_math_operations.py
import pytest
from math_operations import add, subtract, multiply, divide

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 1) == 5

    with pytest.raises(ValueError):  # 測試除以0的情況
        divide(10, 0)