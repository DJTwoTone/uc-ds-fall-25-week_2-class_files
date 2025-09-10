# tests/test_slide17_example.py
import pytest
from slide17_pytest_primer_function import add

def test_add_basic():
    assert add(2, 3) == 5