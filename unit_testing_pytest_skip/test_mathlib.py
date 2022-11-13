import mathlib
import pytest
# import sys

# @pytest.mark.skip(reason="I don't want.") # to skip test
# @pytest.mark.skipif(sys.version_info<(3,5), reason="Cuz version is greater than 3.5") # to skip test when a specific condtion meet
def test_calc_total():
    total=mathlib.calc_total(4,5)
    assert total==9

def test_calc_multiply():
    result=mathlib.calc_multiply(10,3)
    assert result==30

# custom markers
# in this example we could use -k but that is not very efficient for all the cases with different different names
@pytest.mark.windows # showing warnings
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True