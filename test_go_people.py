import pytest
from go_people import check_list

#TESTING LIST CHECKING FOR REMOVING FROM LIST 
def test_check_list_conatining():
    #Testing for when the list conatins the choice
    choice = 1
    list = [1,2,3,4]
    expected_result = [2,3,4]
    assert check_list(list,choice) == expected_result

def test_check_list_notcontaining():
    #Testing for when the list does not contain the choice
    choice = 10
    list = [1,2,3,4]
    expected_result = [1,2,3,4]
    assert check_list(list,choice) == expected_result