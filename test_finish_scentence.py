import pytest
from finish_scentence import check_first5
from finish_scentence import check_lmnop

#TESTING FUNCTION FUNCTION THAT RETURNS TRUE IF A B C D OR E ARE IN THE STRING
def test_check_first5_corr():
    #test with a word that contains a,b,c,d or e
    word = "abacadabra"
    expected_result = True
    assert check_first5(word) == expected_result

def test_check_first5_incorr():
    #test with a word that does not contain a,b,c,d or e
    word = "timid"
    expected_result = False
    assert check_first5(word) == expected_result

#TESTING FUNCTION THAT RETURNS TRUE IF L M N O P ARE IN THE STRING

def test_check_lmnop_corr():
    #test with a word that contains l,m,n,o or p
    word = "london"
    expected_result = True
    assert check_lmnop(word) == expected_result

def test_check_lmnop_incorr():
    #test with a word that does not contain l,m,n,o or p
    word = "read"
    expected_result = False
    assert check_lmnop(word) == expected_result
