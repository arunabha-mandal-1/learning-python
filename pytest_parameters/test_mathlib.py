# combine multiple test cases in a single test case using pytest parameters
import mathlib

# multiple test caes : there is a repeation
# def test_calc_sq_1():
#     result=mathlib.calc_square(5)
#     assert result==25

# def test_calc_sq_2():
#     result=mathlib.calc_square(6)
#     assert result==36

# def test_calc_sq_3():
#     result=mathlib.calc_square(10)
#     assert result==100

# combining
# def test_calc_sq(test_input, expected_output):
#     result=mathlib.calc_square(test_input)
#     assert result==expected_output

import pytest

# we should do this when we deal with similar test caese
@pytest.mark.parametrize("test_input, expected_output",[
    # pass these as tuples
    (5,25),
    (9,81),
    (10,100)
])
def test_calc_sq(test_input, expected_output):
    result=mathlib.calc_square(test_input)
    assert result==expected_output