import time
from RobotFight import Rmain
from game_over import player_death
from house_game import start_house_game
from follow_light import light_game
from go_people import connect_people
from StayStill import make_choice
def StartGame():
    AnimationSpace = 10
    AnimationTime = 0.5
    print("Welcome")
    time.sleep(AnimationTime)
    print("To")
    time.sleep(AnimationTime+1)
    print("Starting Story...")
    time.sleep(AnimationTime)
    print("Teleporting Player...")
    time.sleep(AnimationTime)
    print("Finishing Rendering...")
    time.sleep(AnimationTime)
    print("Goodluck :)")
    print(" ")
    print(" ")
    time.sleep(AnimationTime+2)
    print("Stuck In The Terminal: A Choose Your Own Adventure Game")
    time.sleep(AnimationTime)
    print("Make Choices, Get Lucky, Use Some Skill, and Get Out of The Terminal!")
    for i in range (AnimationSpace):
        print(" ")
    FirstAnim()

def FirstAnim():
    if (input("Write the words skip and click enter to skip, otherwise just click enter to continue:  ")) == "skip".strip():
        print("Make Selection Now:")
    else: 
        with open("First Anim.txt",'r') as FirstScene:
            LengthLineReading = 5 #StartWithAverage 5Seconds
            for line in FirstScene:
                time.sleep(LengthLineReading/18)
                print(line)
                LengthLineReading = len(line)
    ProperSelection = False
    while ProperSelection == False:
        Choice = input()
        if Choice == "1" or Choice == "2" or Choice == "3":
            Choice = int(Choice)
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
        if ReadLine == "S":
            make_choice()
        elif ReadLine == "C":
            is_chosen = False
            while is_chosen == False:
                choice_opp = input()
                if choice_opp == "1" or choice_opp =="2" or choice_opp =="3":
                    choice_opp = int(choice_opp)
                    is_chosen = True
                else:
                    print("Choose a valid option please")
            if choice_opp == 1:
                light_game()
            elif choice_opp == 2:
                connect_people()
            elif choice_opp == 3:
                print("Probably not the best idea, screaming into a void of nothingness, hoping for some result")
                time.sleep(3)
                print("Those sounds of people are gone, but you hear a loud screeching noise approaching you")
                time.sleep(3)
                print("and as it gets locer you sit there and realise your fate")
                time.sleep(1.5)
                print("Goodbye, fair soldier")
                time.sleep(1)
                player_death()
                
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
            if choice == "1" or choice =="2":         
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