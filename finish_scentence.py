import time
from game_won import player_escapes

def main():
    return



def check_first5(word): #Check first letters of alphabet
    for i in range (len(word)-1):
        if word[i] == "a" or word[i] == "b" or word[i] == "c" or word[i] == "d" or word[i] == "e":
            return True
    return False

def check_lmnop(word):
    for i in range (len(word)-1):
        if word[i] == "l" or word[i] == "m" or word[i] == "n" or word[i] == "o" or word[i] == "p":
            return True
    return False





def first_scentence(): #Create Function for first Scentence
    meets_criteria = False #Create Variable for meeting the needed criteria for scnentence
    while meets_criteria == False:
        word = input("I am most thankful for ________ in my life (Must include atleast one letter from the first 5 in the alphabet):  ")
        meets_criteria = check_first5(word)
        if meets_criteria == False:
            print("Make Sure You meat the criteria and try again!")
    print("So Your Scentence is:")
    print(f"I am most thankful for {word} in my life")
    print("Great Job")


def second_scentence(): #Create Function for second Scentence
    meets_criteria = False #Create Variable for meeting the needed criteria for scnentence
    while meets_criteria == False:
        word = input("If I could only live with one item for the rest of my life it would be ________ (Cannot include any of the letters from the first 5 in the alphabet):  ")
        meets_criteria = check_lmnop(word)
        if meets_criteria == False:
            print("Make Sure You meat the criteria and try again!")
    print("So Your Scentence is:")
    print(f"If I could only live with one item for the rest of my life it would be {word}")
    print("Cool")


def third_scentence(): #Create Function for third Scentence
    meets_criteria = False #Create Variable for meeting the needed criteria for scentence
    while meets_criteria == False:
        word = input("I think life is meant for ______ (must contain l,m,n,o or p):  ")
        meets_criteria = check_lmnop(word)
        if meets_criteria == False:
            print("Make Sure You meat the criteria and try again!")
    print("So Your Scentence is:")
    print(f"I think life is meant for {word}")
    print("Meaningful!")


def fourth_scentence(): #Create Function for fourth Scentence
    meets_criteria = False #Create Variable for meeting the needed criteria for scentence
    while meets_criteria == False:
        word = input("I am proud to have ________ in my life (cannot contain l,m,n,o or p):  ")
        meets_criteria = not check_lmnop(word)
    if meets_criteria == False:
            print("Make Sure You meat the criteria and try again!")
    print("So Your Scentence is:")
    print(f"I am proud to have {word} in my life")
    print("Inspirational!")



def startscentence_game():
    with open("light_win.txt","r") as scentencegame_txt:
        #Set Original Time
        LengthLineReading = 60
        for line in scentencegame_txt:
            time.sleep(LengthLineReading/18)
            print(line.rstrip('\n'))
            LengthLineReading = len(line) # Make Reading Length Based on line
    first_scentence()
    second_scentence()
    third_scentence()
    fourth_scentence()
    print("Master Jeff: 'Goodjob, I hope You learnt something boy!' ")
    time.sleep(1.5)
    player_escapes()

if __name__ == "__main__":
    main()