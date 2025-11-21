
# How to Test

Pytesting 

 

For pytesting all the logic that returns a value and does not take a user input must be tested. When testing it is necessary to test the boundries of the function. So for example, if a function returns a number from 1 – 90, you would test the function with parameters that return 1, and with parameters that return 90. Testing the boundaries 

 

It is also very important to focus on functions that must return a certain value, and testing values that are outside the range to make sure the return is valid. For example, if the function does a list search, you should check what happens when the index is not in the list (usually returns –1) 

 

I majorly used pytest for each game, as the games contain logic that has to be calculated and is not just based off user input.  

 

Here are some of the pytests being run: 

 

test_robot_fight.py - Used to test damage to player and robot Aswell as player and robot death 

 

test_house_game.py - Used to test the checking of correct answer in the quote house game 

 

test_follow_light.py - Used to test the function that calculates distance based off projectile motion 

 

test_jeff_trivia.py - Used to test the checking of correct answer for the trivia/riddle  game 

 

test_finish_scentence.py - Tests the functions that check if a string contains a certain letter such as (a b c d e or f).  

 

Test_go_people.py - Used to test the function that intakes a list and a int, searches for the int in the list and removes it. 

 

Running the Pytests: 

 

Run these commands to test Pytest 

To test the whole repo: pytest 

 

To test whole repo with additional info: pytest –verbose 

 

To test individual test file: pytest –verbose [file name] 