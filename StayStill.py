import random
import time
from game_over import player_death
from game_won import player_escapes
from follow_light import light_game
from jeff_trivia import start_trivia
def main():
    return
def make_choice():
    chocie_made = False
    while chocie_made == False:
        choice = input()
        if choice == "1" or choice == "2":
            choice = int(choice)
            chocie_made = True
        else:
            "Please make a correct choice"
    if choice == 1:
        roll_to_win()
    elif choice == 2:
        point_direction()
def roll_to_win():
    roll = random.randint(1,20)
    print("ok the random number has been chosen...")
    time.sleep(2.5)
    print("Now time for you to choose and try to get the right number")
    time.sleep(1)
    guess_made = False
    while guess_made == False:
        guess = int(input("Guess Here (1-20):  "))
        if guess <= 20 and guess >= 1:
            guess_made = True
        else:
            "Please enter a correct number within the range."
    if roll == guess:
        print(f"Wow the number was {roll} you guessed it, goodjob you escape! ")
        player_escapes()
    else:
        print(f"Wow the number was {roll} you shouldve known better than to gamble it all away... ")
        player_death()
        
def point_direction():
    print("Ok well there are actually two directions I can point you in, its up to you where you want to go...")
    time.sleep(3)
    print("There is a nice little lightbulb in one direction, and I think I saw Master Jeff go another direction")
    time.sleep(2) 
    print("That is for you to decide...")
    print(".....................")
    time.sleep(2)
    print("Type 1 to go towards the light")
    print("Type 2 to go where Master Jeff Might be...")
    choice_made = False
    while choice_made == False:
        choice = input()
        if choice == "1" or choice == "2":
            choice_made = True
            choice = int(choice)
        else:
            print("Please make a proper slection (1 or 2)")
    if choice == 1:
        light_game()
    elif choice ==2:
        start_trivia()


if __name__ == "__name__":
    main()