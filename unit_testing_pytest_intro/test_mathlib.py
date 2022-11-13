# you have to have a prefix of 'test_' for unit test file
# unit test for functions in mathlib.py
import mathlib

# always give 'test_' prefix to all the functions as well as file names
def test_calc_total():
    total=mathlib.calc_total(4,5)
    assert total==9

def test_calc_multiply():
    result=mathlib.calc_multiply(10,3)
    assert result == 30