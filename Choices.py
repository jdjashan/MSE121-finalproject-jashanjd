import time

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
            time.sleep(LengthLineReading/12)
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
            if Choice == 1:
                print()
                #FuncInput
            elif Choice == 2:
                print()
                #FuncInput
            elif Choice == 3:
                print()
                #FuncInput
        else: 
            time.sleep(LengthLineReading/12)
            print(ReadLine.rstrip('\n'))
            LengthLineReading = len(line) # Make Reading Length Based on line







def main():
    return






















if __name__ == "__main__":
    main()