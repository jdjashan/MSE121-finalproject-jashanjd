import pytest
from follow_light import calc_range_height_tot
from follow_light import try_light_max
from finish_scentence import check_first5
from finish_scentence import check_lmnop
from go_people import check_list
from RobotFight import calc_damage
#This File contains the extra test functions to make sure that all the functions are compeltely working

#Test light game projectile for max distance
def test_calc_range_height_max():
    optimal_angle = 52.02 #Used AI to find optimal angle
    max_height = 3.169734
    max_range = 9.899413 
    expected_result = max_height + max_range
    
    assert calc_range_height_tot(optimal_angle) == pytest.approx(expected_result) 

#Test light game max for when equal
def test_light_max_equal():
    #test for when current distance is equal to previous max
    curr_value = 0.1
    max_value = 0.1
    expected_result = curr_value, max_value #Should only return both curr if curr is greate not equal

    assert try_light_max(curr_value,max_value) == expected_result 

    #Test light game max for when extremely close (spproximation)
def test_light_max_close():
    #test for when current distance is greater that previous max
    curr_value = 0.000032
    max_value = 0.000023
    expected_result = curr_value, curr_value #curr_value slightly higher
    assert try_light_max(curr_value,max_value) == expected_result 

#Lets test the scentence game function that tests for a b c d or e in a string

#Test for when there is only a
def test_check_first5_one_a():
    #test with a word that contains only a out of first five
    word = "tall"
    expected_result = True
    assert check_first5(word) == expected_result

#Test when only b
def test_check_first5_one_b():
    #test with a word that contains only b out of first five
    word = "bun"
    expected_result = True
    assert check_first5(word) == expected_result

#Test when only c
def test_check_first5_one_c():
    #test with a word that contains only c out of first five
    word = "cross"
    expected_result = True
    assert check_first5(word) == expected_result

#Test when only d
def test_check_first5_one_d():
    #test with a word that contains only d out of first five
    word = "doom"
    expected_result = True
    assert check_first5(word) == expected_result

#Test when only e
def test_check_first5_one_e():
    #test with a word that contains only e out of first 5
    word = "eel"
    expected_result = True
    assert check_first5(word) == expected_result

#Test when all letters
def test_check_first5_all():
    #test with a word that contains all letetrs from first five in alphabet
    word = "backed"
    expected_result = True
    assert check_first5(word) == expected_result

#Lets test the scentence game function that tests for l m n o or p in a string

#Test for when there is only l
def test_check_lmnop_one_l():
    #test with a word that contains only l out of lmnop
    word = "lick"
    expected_result = True
    assert check_lmnop(word) == expected_result

#Test when only m
def test_check_lmnop_one_m():
    #test with a word that contains only m out of lmnop
    word = "make"
    expected_result = True
    assert check_lmnop(word) == expected_result

#Test when only n
def test_check_lmnop_one_n():
    #test with a word that contains only n out of lmnop
    word = "nuke"
    expected_result = True
    assert check_lmnop(word) == expected_result

#Test when only o
def test_check_lmnop_one_o():
    #test with a word that contains only o out of lmnop
    word = "over"
    expected_result = True
    assert check_lmnop(word) == expected_result

#Test when only p
def test_check_lmnop_one_p():
    #test with a word that contains only p out of lmnop
    word = "peak"
    expected_result = True
    assert check_lmnop(word) == expected_result

#Test when all letters
def test_check_lmnop_all():
    #test with a word that contains all letters in lmnop
    word = "policeman"
    expected_result = True
    assert check_lmnop(word) == expected_result


#Test List checking function that removes found indexes

#Test with multiple occurances of the guess
def test_check_list_containing_double():
    #Should return a list with the first occurance removed only
    choice = 5
    list = [5,5,3,4,3,5]
    expected_result = [5,3,4,3,5]
    assert check_list(list,choice) == expected_result

#Test with only the occurance being the guess
def test_check_list_containing_single():
    #Should return a empty
    choice = 0
    list = [0]
    expected_result = []
    assert check_list(list,choice) == expected_result



#Test the robot damage feature

#Test damage with 0
def test_damage_both_zero():
    #Test with two 0 lists
    expected_result = 0
    assert calc_damage([0],[0]) == expected_result


#Test damage with one list being zero
def test_damage_one_zero():
    #Test with one list being 0
    expected_result = 0
    assert calc_damage([1],[0]) == expected_result