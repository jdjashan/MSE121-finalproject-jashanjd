import pytest
from RobotFight import calc_damage
from RobotFight import health_loss



# TESTS FOR FUNCTION DEALING DAMAGE
def test_damage_one():
    #Test with 3 and 5
    expected_result = 15
    assert calc_damage([3],[5]) == expected_result
def test_damage_two():
    #Test with 3,3 and 5,5
    expected_result = 15 + 18
    assert calc_damage([3,3],[5,6]) == expected_result
def test_health_loss_one():
    #Test with choice one, no poisin damage
    # Result will just be health - damage
    expected_result = 75 - 25

    #We must make some assumptions to test, assume health is 75, assume damage is 25, assume there is no current poisin, place player or Robot, does not matter
    assert health_loss(25,1,75,0,"Robot") == expected_result

def test_health_loss_two():
    #Test with choice two, some poisin damage
    # Result will just be health - damage(maxed at 15) - poisin/5
    expected_result = 100 - 15 - 50/5

    #We must make some assumptions to test, assume health is 100, assume damage is 25(maxed at 15), assume poisin is at 50 right now, place player or Robot, does not matter
    assert health_loss(25,2,100,50,"Robot") == expected_result



#TESTING RETURN STATEMNTS FOR ROBOT AND PLAYER
def test_health_loss_robo_death():
    #Test with choice one, no poisin
    # Result should return 0, because dead
    expected_result = 0

    #We must make some assumptions to test, assume health is 25, assume damage is 50, assume there is no current poisin, We are checking Robot Death so place Robot
    assert health_loss(50,1,25,0,"Robot") == expected_result

def test_health_loss_player_death():
    #Test with choice two, some poisin damage
    # Result should return 0, because dead
    expected_result = 0

    #We must make some assumptions to test, assume health is 50, assume damage is 50(maxed at 15), assume there is 50 current poisin, We are checking Player Death so place Player
    assert health_loss(50,2,20,50,"Player") == expected_result

def main():
    return






if __name__ == "__main__":
    main()