import time
from game_won import player_escapes


def main():
    return

def corr_person(): #Function is used to show user all oppurtunities
    person_list = [1,2,3,4,5,6,7,0]
    print("Based off your personality who could you be friends with. Enter the Persons Number as the answer")
    while len(person_list) > 1:
        choice_made = False
        while choice_made == False:
            choice_person = input() 
            if choice_person == "1" or choice_person == "2" or choice_person == "3" or choice_person == "4" or choice_person == "5" or choice_person == "6" or choice_person == "7":
                choice_person = int(choice_person)
                choice_made = True
            if choice_made == False:
                print("Make A Valid Selection Please")
        for i in range (len(person_list)-1):
            if person_list[i] == choice_person:
                person_list.pop(i)
                print(person_list)
                break
        if len(person_list) > 1:
            print(" And?, Anyone Else you might be able to be freinds with?")

    print("exactly, the point that is to be made, is that anyone can be friends with another, in life are all humans")
    time.sleep(2)
    print(" Its also important to remember that 2 toonies is better than 30 dimes, those close freinds are always worth more than a bunch of accomplices... ")
    time.sleep(3)
    print("A quote by Barney says: 'whatever you do in this life, its not legendary unless your friends are there to see it' ")
    time.sleep(3)
    print("Time will try to rip those close relationsips apart, but dont let it, those connections are some of the most important parts of your life... ")
    time.sleep(3)
    print("Master Jeff: 'The purpose of this game was to teach you, help you realise more about the meaning of life, and I think you suceeded. So here is 10 points son.")
    time.sleep(2)
    player_escapes()




def connect_people():
    with open("go_people.txt",'r') as people_text:
        LengthLineReading = 30 #StartWithAverage 5Seconds
        for line in people_text:
            time.sleep(LengthLineReading/18)
            print(line)
            LengthLineReading = len(line)
    corr_person()
    




if __name__ == "__main__":
    main()