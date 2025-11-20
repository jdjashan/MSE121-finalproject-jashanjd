import time
from house_game import start_house_game
from game_over import player_death


def main():
    return


def check_answer(guess,correct_guess):
    if guess == correct_guess:
        return(1)
    else:
        return(0)

def riddle_1(points):
    print("Master Jeff: 'First Riddle:")
    time.sleep(1)
    print("Master Jeff:  'What is so fragile that just saying its name breaks it?' ")
    time.sleep(2)
    print("Type 1 for Glass")
    print("Type 2 for Silence")
    print("Type 3 for Love")
    choice_made = False
    while choice_made == False:
        choice = input()
        if choice == "1" or choice == "2" or choice == "3":
            choice = int(choice)
            choice_made = True
        else:
            print("Please choose a valid choice!")
    
    points = points + check_answer(choice,2)


def trivia_2(points):
    print("Master Jeff: 'First Trivia:")
    time.sleep(1)
    print("Master Jeff:  'How many hours are in a day?' ")
    time.sleep(2)
    print("Type 1 for 12")
    print("Type 2 for 24")
    print("Type 3 for 25")
    choice_made = False
    while choice_made == False:
        choice = input()
        if choice == "1" or choice == "2" or choice == "3":
            choice = int(choice)
            choice_made = True
        else:
            print("Please choose a valid choice!")
    print("The correct answer is 24, We all know it’s 24, but no matter who you are, everyone gets the same amount.")
    time.sleep(2)
    print("Time is one of the few things in life that’s perfectly fair—what you do with it is what makes the difference.")
    time.sleep(2)
    points = points + check_answer(choice,2)

def riddle_3(points):
    print("Master Jeff: 'Riddle Now:")
    time.sleep(1)
    print("Master Jeff:  'I follow you everywhere, But I never take a step. I grow when you face the light and vanish when you hide from it. What am I?' ")
    time.sleep(2)
    print("Type 1 for Shadow")
    print("Type 2 for Pride")
    print("Type 3 for Dignity")
    choice_made = False
    while choice_made == False:
        choice = input()
        if choice == "1" or choice == "2" or choice == "3":
            choice = int(choice)
            choice_made = True
        else:
            print("Please choose a valid choice!")
    print("Your “dark parts” aren’t dangerous—they simply grow or shrink depending on how much light you allow into your life.")
    time.sleep(3.5)
    points = points + check_answer(choice,2)


def start_trivia():
    with open("jeff_trivia.txt","r") as trivia_txt:
        #Set Original Time
        LengthLineReading = 36
        for line in trivia_txt:
            time.sleep(LengthLineReading/18)
            print(line.rstrip('\n'))
            LengthLineReading = len(line) # Make Reading Length Based on line
    trivia_points = 0
    trivia_points = riddle_1(trivia_points)
    trivia_points = trivia_2(trivia_points)
    trivia_points = riddle_3(trivia_points)
    if trivia_points >= 2:
        print("Master Jeff: 'Goojob you beat 2 points, and your ready for the house game in the house of wisdom. Just find the hidden meeting of some quotes for me")
        start_house_game()
    else:
        print("Master Jeff 'Im sorry son, you did not finish with over 2 out of 3 correct, your time has come")
        player_death()




if __name__ == "__main__":
    main()