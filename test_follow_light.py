import pytest
from follow_light import calc_range_height_tot
from follow_light import try_light_max

#TESTING FUNCTION THAT CALCULATES TOTAL HEIGHT AND DISTANCE
def test_calc_range_height_90():
    # Testing with a shot of 90 degrees

    expected_height = 5.10204 #Calculated from hand
    expected_distance = 0
    assert calc_range_height_tot(90) == pytest.approx(expected_distance + expected_height)

def test_calc_range_height_0():
    #Testing with 0 degrees

    expected_height = 0  #Both Zero because sin(0) is 0
    expected_distance = 0
    assert calc_range_height_tot(0) == pytest.approx(expected_distance + expected_height)

def test_calc_range_height_45():
    #Testing with midpoint at 45 degrees

    expected_height = 2.5510204  #Calculated from hand
    expected_distance = 10.2040816 #Calculated from hand
    assert calc_range_height_tot(45) == pytest.approx(expected_distance + expected_height)

#TESTING FUNCTION THAT COMPARES CURRENT DISTANCE TO MAX DISTANCE

def test_light_max_greater():
    #test for when current distance is greater that previous max
    curr_value = 5
    max_value = 4
    expected_result = curr_value, curr_value
    assert try_light_max(curr_value,max_value) == expected_result

def test_light_max_less():
    #test for when current distance is greater that previous max
    curr_value = 5
    max_value = 10
    expected_result = curr_value, max_value
    assert try_light_max(curr_value,max_value) == expected_result

