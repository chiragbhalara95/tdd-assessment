import pytest
import sys
import os

# Add src/ folder to Python path (Windows-friendly)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from string_calculator import StringCalculator, NegativesError

calc = StringCalculator()

def test_empty_string_returns_0():
    assert calc.add("") == 0

def test_single_number_returns_value():
    assert calc.add("1") == 1

def test_two_numbers_comma():
    assert calc.add("1,5") == 6

def test_many_numbers_sum():
    assert calc.add("1,2,3,4") == 10

def test_newlines_between_numbers():
    assert calc.add("1\n2,3") == 6

def test_custom_single_char_delimiter():
    assert calc.add("//;\n1;2") == 3

def test_negative_raises_exception_and_lists_all():
    with pytest.raises(NegativesError) as exc:
        calc.add("2,-4,3,-5")
    msg = str(exc.value)
    assert "-4" in msg and "-5" in msg
