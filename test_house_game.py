import pytest
from house_game import check_correct


#TEST FUNCTION THAT RETURNS 1 FOR CORRECT ANSWER AND 0 FOR INCORRECT BY COMPARING CORRECT AND GIVEN ANSWER 
def test_check_correct_corr():
    #Test if returns 1 for correct answer
    corr_answer = 1
    given_answer = 1
    expected_result = 1
    assert check_correct(corr_answer,given_answer) == expected_result


def test_check_correct_incorr():
    #Test if returns 0 for incorrect answer
    corr_answer = 1
    given_answer = 2
    expected_result = 0
    assert check_correct(corr_answer,given_answer) == expected_result