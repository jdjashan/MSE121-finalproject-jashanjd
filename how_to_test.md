
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




Manual Testing 

 

Manual testing for a game such as this can get pretty confusing, with many  different possibilities of user inputs. We will go over all the base win and loss cases, more will be covered later on the test_coverage.md 

 

*Each input is separated by a double space 

 

*Enter represents just hitting enter key in keyboard 

 

Winning inputs: 

 

Enter  1  1  1  1  1  2  1  1  3  2   ---- (Assuming Player wins Robot Fight and gets all House game questions right) 

 

Enter 2  1  40  45  50  55  53  family  gold  love  sister  ----(Assuming Player gets the light projectile passed and completes sentence game) 

 

Enter 2  2  1  2  3  4  5  6  7  ----(Assuming Player chooses all people and wins game) 

 

Enter 3 1 18 ----(Assuming Player guess correct random number) 

 

Enter 3 2 1  40  45  50  55  53  family  gold  love  sister  ----(Assuming Player gets the light projectile passed and completes sentence game) 

 

Enter 3  2  2  2  2  1  2  1  1  3  2  ----(Assuming Player gets every trivia/riddle and then gets every quote interpretation correct) 

 

Losing Inputs:  

 

Enter 1  1  1  1 ----(Assuming Player Loses to Robot) 

 

Enter  1  1  1  1  1  1  1  2  2  3  ----(Assuming Player beats robot but loses to the house game by getting all answers incorrect) 

 

Enter  2  1  10  15  20  25  30  ----(Player loses the light projectile game) 

 

 

Enter  2  3  ----(Player dies to unknown screeching figure) 

 

Enter  3  1  10  ----(Assuming Player does not guess the number correctly to escape the game) 

 

Enter  3  2  1  10  15  20  25  30  ----(Player loses light projectile game) 

 

Enter  3  2  2  1  1  2  ----(Player loses by getting all riddle/trivia wrong) 

 

Enter  3  2  2  1 2  2  1  1  2  2  3  ----(Player loses by winning light game but then losing house game – quote interpretation getting all wrong) 