import time
from game_won import player_escapes

def main():
    return
def start_house_game():
    game_points = 0
    game_points = quote_1(game_points)
    game_points = quote_2(game_points)
    game_points = quote_3(game_points)
    game_points = quote_4(game_points)
    game_points = quote_5(game_points)
    if game_points >= 3:
        player_escapes()
    else:
        print("Master Jeff: 'Im Sorry Young Soldier, your time has come.' ")

def check_correct(corr_answer,given_answer):
    if corr_answer == given_answer:
        print("Correct")
        return (1)
    else:
        print("Incorrect")
        return (0)
def quote_1(Points):  
    print("Master Jeff 'Ok Lets Start Easy:")
    time.sleep(2)
    print("Yesterday is History, Tommorow is a Mystery, but Today is a gift that is why it is called the Present ")
    time.sleep(3.5)
    print("What is the quotes meaning?")
    time.sleep(1.5)
    print("Type 1 : Start Planning for Your Future Now" )
    print("Type 2 : The Time you have is scarce and unknown, so enjoy the Moment")
    print("Type 3 : Lessons from your past are valuable, make sure you think back and remember.")
    choice_made = False
    choice = input()
    while choice_made == False:
        if choice == "1" or "2" or "3":
            choice = int(choice)
            choice_made = True
    Points = Points + check_correct(2,choice)
    return Points

def quote_2(Points):  
    print("Master Jeff 'A little harder now!:")
    time.sleep(2)
    print("Life is a Line, there are twists and turns, but no roundaabouts, no u-turns. Just a long road ahead, you can think back, but never go back. The intersections with other lines are the people you meet along the way, remember to enjoy those intersections.")
    time.sleep(3.5)
    print("What is the quotes meaning?")
    time.sleep(1.5)
    print("Type 1 : You are always moving forward in life, meeting new people and finding new meaning, make the most of it" )
    print("Type 2 : There are so many twists and turns in life, and its impossible to reverse them. Try to not get lost.")
    print("Type 3 : Life is full of intersections, lines and people. Try to straighten that line out as much as possible.")
    choice_made = False
    choice = input()
    while choice_made == False:
        if choice == "1" or "2" or "3":
            choice = int(choice)
            choice_made = True
    Points = Points + check_correct(1,choice)
    return Points

def quote_3(Points):  
    print("Master Jeff 'Ok the quotes are really getting good':")
    time.sleep(2)
    print("It ain't what they call you, it's what you answer to")
    time.sleep(3.5)
    print("What is the quotes meaning?")
    time.sleep(1.5)
    print("Type 1 : You make your own self worth, your response to others words are worth far more than what they say" )
    print("Type 2 : Your name holds worth, dont let others abuse that worth and not name you correctly.")
    print("Type 3 : Your legacy is built off what your are called, and how people name you. Dont let others tell you who your meant to be")
    choice_made = False
    choice = input()
    while choice_made == False:
        if choice == "1" or "2" or "3":
            choice = int(choice)
            choice_made = True
    Points = Points + check_correct(1,choice)
    return Points
def quote_4(Points):  
    print("Master Jeff 'Hmm, how about this one from Master Oogway':")
    time.sleep(2)
    print("You can choose where to plant a peach tree, but you cannot control what the tree grows to be, you can hope for an apple, or orange. But you will get a peach.")
    time.sleep(3.5)
    print("What is the quotes meaning?")
    time.sleep(1.5)
    print("Type 1 : Trees are stubborn, just like human civilization, we need to learn to adapt and grow differently" )
    print("Type 2 : No one can control what they do, or who they are. They can only ride the flow and try thier best")
    print("Type 3 : You cannot force something to be what it is not, but you can nurture and believe in it to help it reach its full potential.")
    choice_made = False
    choice = input()
    while choice_made == False:
        if choice == "1" or "2" or "3":
            choice = int(choice)
            choice_made = True
    Points = Points + check_correct(3,choice)
    return Points
def quote_5(Points):  
    print("Master Jeff 'Ok Final One, Lets End it Good':")
    time.sleep(2)
    print("If oppurtunity doesnt knock, build a door ")
    time.sleep(3.5)
    print("What is the quotes meaning?")
    time.sleep(1.5)
    print("Type 1 : Oppurnutnity is about finding doors, and opening them. To reach your full oppurunity you must open those doors" )
    print("Type 2 : Oppurtunity is Created not Found, when you arent given oppurtunity make it yourself!")
    print("Type 3 : Wait for just the right time, then take that oppurtunity and ride it to the end!")
    choice_made = False
    choice = input()
    while choice_made == False:
        if choice == "1" or "2" or "3":
            choice = int(choice)
            choice_made = True
    Points = Points + check_correct(2,choice)
    return Points


if __name__ == "__main__":
    main()