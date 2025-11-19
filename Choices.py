import time
from RobotFight import Rmain
from game_over import player_death
from house_game import start_house_game
def StartGame():
    AnimationSpace = 10
    AnimationTime = 0.5
    print("Welcome")
    time.sleep(AnimationTime)
    print("To")
    time.sleep(AnimationTime+1)
    print("(^V^)--1")
    time.sleep(AnimationTime)
    print("(@_@)--2")
    time.sleep(AnimationTime)
    print("(<_>)--3")
    time.sleep(AnimationTime)
    print("(*o*)--4")
    time.sleep(AnimationTime+2)
    print("Stuck In The Terminal: A Choose Your Own Adventure Game")
    time.sleep(AnimationTime)
    print("Make Choices, Get Lucky, Use Some Skill, and Get Out of The Terminal!")
    for i in range (AnimationSpace):
        print(" ")
    FirstAnim()

def FirstAnim():
    with open("First Anim.txt",'r') as FirstScene:
        LengthLineReading = 5 #StartWithAverage 5Seconds
        for line in FirstScene:
            time.sleep(LengthLineReading/18)
            print(line)
            LengthLineReading = len(line)
    ProperSelection = False
    while ProperSelection == False:
        Choice = int(input())
        if Choice == 1 or 2 or 3:
            ProperSelection = True
        else:
            ProperSelection = False
            print("Please Choose One of the available options!")
        
    FirstChoiceMade(Choice)


def FirstChoiceMade(Choice):
    if Choice == 1:
        Storyline = open("FollowJeff.txt",'r')
    elif Choice == 2:
        Storyline = open("OppositeJeff.txt",'r')
    elif Choice == 3:
        Storyline = open("StayStill.txt",'r')
    LengthLineReading = 12 #StartWithAverage 12 Seconds for reading
    for line in Storyline:
        ReadLine = line
        if ReadLine == "D":
            print()
            #DeathFunc
        elif ReadLine == "C":
            is_chosen = False
            choice_opp = input()
            while is_chosen == False:
                if choice_opp == "1" or "2" or "3":
                    choice_opp = int(choice_opp)
                    is_chosen = True
            if choice_opp == 1:
                print()
                #FuncInput
            elif choice_opp == 2:
                print()
                #FuncInput
            elif choice_opp == 3:
                print()
                #FuncInput
        elif ReadLine.strip() == "G":
            robot_win_choice(Rmain())
        else: 
            time.sleep(LengthLineReading/18)
            print(ReadLine.rstrip('\n'))
            LengthLineReading = len(line) # Make Reading Length Based on line
    

def robot_win_choice(choice):
    if choice == 1:
        print ("Soooo.... it wasnt a loot bag. It was a bomb, sorry player...")
        player_death()
    elif choice == 2:
        with open("leave_lootbag.txt","r") as lootbag_txt:
        #Set Original Time
            LengthLineReading = 36
            for line in lootbag_txt:
                time.sleep(LengthLineReading/18)
                print(line.rstrip('\n'))
                LengthLineReading = len(line) # Make Reading Length Based on line
        choice_made = False
        choice = input()
        while choice_made == False:   
            if choice == "1" or "2":         
                choice = int(choice)
                choice_made = True
        enter_house_choice(choice)    



def enter_house_choice(choice):
    if choice == 1:
        start_house_game()
    elif choice == 2:
        print("You walk around for a while but it starts getting really cold")
        time.sleep(3)
        print("It gets so cold, you stop moving, and boom just like that, you cannot feel your body")
        time.sleep(3)
        player_death()
        
       





def main():
    return






















if __name__ == "__main__":
    main()