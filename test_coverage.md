
# Test Coverage

Here I will cover the additional pytest cases, and all the manual testing required for the outcomes! 

 

Pytests 

 

The additional pytests considered more than just the boundries but also the extra possibilities that came with every function 

 

The functions that were additionally pytested were: 

 

The damage robot feature  

Test damage when both lists are 0 

Test damage when only one list is 0 

Both have expected_result 0. 

 

Testing removal of items from a list feature 

Testing when you have duplicates in list 

Expected_result has the first index removed but keeps the other duplicates in place 

For example, 

The input is 3 

[3,1,2,3,3,4]   to  [1,2,3,3,4] 

 

Testing when the list only has the guess in it and nothing else 

Expected_result has an empty list that removes the last index in the list 

For example, 

Input is 4 

[4]   to   [] 

 

Testing the letter check, both lmnop and first five from alphabet 

Test each letter separately when only one is present in the word 

They should all yield the same expected_result which is True. It just checks to make sure that the check works for all the letters 

Test when all letters are in the word for both 

They should both yield True, this just makes sure that having all of them does not cause any unneeded bugs 

 

Testing for the light game 

Checking when the current and max are equal 

This should not change the max, the function only changes it when current is greater. This confirms no bugs when equal 

 

Checking when they are very close by decimal value 

Should still return the current number is bigger or max number if smaller. Just check for bugs with approximation. 

 

Testing the light projectile distance calculation function 

 

Checking if the distance is correct for the maximum optimal angle 

Should return the highest value calculated by projectile motion eqns, Used secondary reaserch to find optimal angle and made sure the distances matched 

 

 

 

 

 

 

Manual Testing 

 

Manual testing this choose your own story game can get pretty complicated, especially since there are around 2^number of choices there are. Not even including the options with 3 choices. 

 

Im going to show how to test each game manually. It will look like this: 

There will be a path to get to the game, then a list of combinations for the game itself: 

Let's start with: 

Robot Game 

Path to Game: Enter  1   

Possibilities in Game (Very Hard because there are so many possibilities): 

*Though we can make a minimum and maximum assumption  

We know that if the user uses all attack one, the maximum amount of attacks that can be done must be the minimum damage, which is rolling two 1’s. So you can do a total of 1 damage per round.  

With a robot of 100 hp, it would take 100 rounds to defeat the robot 

So the output would be 1 x100 

 

The minimum amount of attacks is created through the maximum amount of damage, which is 36 (by rolling two 6’s) 

With a robot of 100hp it would take 3 rounds to defeat the robot 

 

There the possibilities look something like this 

1  1  1 

1  1  1  1 

1  1  1  1  1 

1  1  1  1  1  1 

All the way untill  

1 x100 

(This does assume that the robot does not kill the player in this time) 

 

*Assuming the player does not die to the bot 

Now for poison it gets slightly more complicated... 

But we can try to follow the same min max assumptions and use those to say that everything in the middle is possible 

 

Lets start with maximum rounds, which funny enough is pretty similar, assuming the user does minimum damage, which would conclude that the user only rolls ones and has two lists of two ones. Leading to a total damage of 2: 

With a robot health of 100 it would take 50 rounds 

The minimum is a little harder, a max damage shot will do 72 damage(lists of all 6’s) but only 15 in the moment. 

So the first round will do 15, the next will do 15 + 11.4, the next will be 15 + 11.4*2, until 100 damage . Which will take 4 rounds.  

 

So the possibilities for poison are 

 

2  2  2  2 

2  2  2  2  2 

Up to 2 x 50 

 

Combinations of poison and basic attacks can arise, but in general, there will be no combo that will take less than 3 rounds, or more than 100 rounds. 

There can be combos such as  

1  2  2  

1  1  2  2  

Here are the possible (extra) tests for the robot game (manual) 

 

Basic 

1  1  1 

1  1  1  1 

1  1  1  1  1 

1  1  1  1  1  1 

Up to 1 x100 

AND 

Poison 

2  2  2  2 

2  2  2  2  2 

Up to 2 x 50 

 

*Chance shot in how_to_test 

 

House Game:  

Enter 1 (Beat Robot) 

Enter 3  2  2 (Beat Trivia) 

Next the house game which contains 3125 different combinations of user input 

 

Here are some examples of possible user inputs: 

1  2  3  4  5 

2  3  4  5  1 

3  4  5  1  2   

 

And there are so many more, the winnign choices are much easier to permute. 

 

2  1  1  3  2 – are the full correct answers 

 

So the user can test these combos and they should win the game: 

(x and y can be any number 1-3) 

 

2  1  1  x  y 

x 1  1  3  y 

x  y  1  3  2 

x  1  y  3  2 

x 1  1  y  2 

2  x  1  3  y 

2  1  x  3  y 

 

 

Finish the sentence has countless strings that fit... 

 

Light Game: 

Enter 2  1 

Enter 3  2  1 

The light game is wierd because, there are soooo many different possibilites. But only a couple logical ones 

 

Assuming the user chooses a new angle every time there are 90! Possibilites, which is crazy 

Though, assuming the user is not dumb, lets say they go to the midpoint and take 10 below and 10 above, and they choose from the new set. Now it is 20! Assuming they choose a new one each time.  

Therefore:  

Between 35 – 55 degrees 

The user has 20! Possibilites 

Though only guesses above 45 will win the user the game! 

 

 

Trivia: Enter 3  2  2 

Trivia is the same premise as the house game, yet this time there are 3 instead of 5. 

So the winning answers are 2  2  1 

There any of these combos will let the player win... 

(x is any number 1-3) 

2  2  x 

x  2  1 

2  x  1 

 

Those are all the extra manual tests! 

