import pytest
from jeff_trivia import check_answer

# TESTS FOR CHECKING ANSWER CORRECTNESS
def test_check_answer_corr():
    #Test when answer is correct
    answer = 1
    guess = 1
    expected_result = 1
    assert check_answer(guess,answer) == expected_result

def test_check_answer_incorr():
    #Test when answer is incorrect
    answer = 1
    guess = 2
    expected_result = 0
    assert check_answer(guess,answer) == expected_result
