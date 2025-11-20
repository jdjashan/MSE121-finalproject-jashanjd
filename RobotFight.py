import random
import time
from game_over import player_death
def fight_explaination():
    with open("robot_fight_ex.txt","r") as robo_txt:
        #Set Original Time
        LengthLineReading = 36
        for line in robo_txt:
            time.sleep(LengthLineReading/18)
            print(line.rstrip('\n'))
            LengthLineReading = len(line) # Make Reading Length Based on line             
def robot_death():
    with open("robot_win.txt","r") as robo_txt:
        #Set Original Time
        LengthLineReading = 48
        for line in robo_txt:
            time.sleep(LengthLineReading/18)
            print(line.rstrip('\n'))
            LengthLineReading = len(line) # Make Reading Length Based on line   
    choice_made = False
    while choice_made == False:
        choice = input().strip()
        if choice == "1" or choice == "2":
            choice_made = True
            choice = int(choice)
        else:
            print("Please Choose a Valid Selection")
    return choice
    
def create_damage_list(Type):
    random1=[]
    random2 = []
    if Type == 1:
        random1.append(random.randint(1,6))
        random2.append(random.randint(1,6))
    elif Type == 2:
        for i in range (1):
            random1.append(random.randint(1,6))
            random2.append(random.randint(1,6))
    return random1,random2
    
def calc_damage (dmg1,dmg2):
    total_dmg = 0
    for i in range (len(dmg1)):
        total_dmg = total_dmg + dmg1[i-1]*dmg2[i-1]
    return total_dmg

def health_loss(Damage,Type,Health,Poisin,ply_or_robo):
    if Type == 1:
        if (Health - Damage - Poisin/5) <=0:
            if ply_or_robo == "Robot":
                print(f"Robot Takes {Damage + Poisin/5} damage which is enough to kill him!")
            else:
                print(f"Dang you take {Damage + Poisin/5} damage and die...")
                player_death()
        else: 
            return (Health - Damage - Poisin/5)
    elif Type == 2:
        if Damage >= 15:
            if (Health - 15 - Poisin/5) <=0:
                if ply_or_robo == "Robot":
                    print(f"Robot Takes {15 + Poisin/5} damage which is enough to kill him!")
                else:
                    print(f"Dang you take {15 + Poisin/5} damage and die...")
                    player_death()
                return 0
            else: 
                return (Health - 15 - Poisin/5)
        else: 
            if (Health - Damage - Poisin/5) <=0:
                if ply_or_robo == "Robot":
                    print(f"Robot Takes {Damage + Poisin/5} damage which is enough to kill him!")
                else:
                    print(f"Dang you take {Damage + Poisin/5} damage and die...")
                    player_death()
                return 0
            else:
                return (Health - Damage - Poisin/5)
    elif Type == 3:
        return 0
def chance_game():
    print("Ok your doing it, taking that chance, goodluck")
    time.sleep(3)
    print(" You have a 1 in 30 chance to guess the random number")
    time.sleep(3)
    print("Enter Your Guess Down Below...")
    time.sleep(3)
    p_guess = int(input())
    game_roll = random.randint(1,30)
    print(f"The random number is: {game_roll}")
    if p_guess != game_roll:
        print("Ooops those are not equal...")
        player_death()

def Rmain():
    RoboHealth = 50
    PlayerHealth = 50
    player_poisin = 0
    robot_poisin = 0
    fight_explaination()
    while (RoboHealth != 0 and PlayerHealth != 0):
        #Player Choice
        print("Type 1 for Basic Attack")
        print("Type 2 for Poisin Attack")
        print("Type 3 for a Chance Attack")
        chosen = False
        while chosen == False:
            type = int(input())
            if type == 1 or 2 or 3:
                chosen = True
            else:
                print("Choose 1, 2 or 3")


        #Create Chance Game for Choice Three
        if type == 3:
            chance_game()
        # Make Random Lists for Damage
        damage1, damage2 = create_damage_list(type)

        #Damage Function using Dot Product of List
        damage_tot = calc_damage(damage1,damage2)

        #Check Poisin Player, and add
        if type == 2 and damage_tot > 15:
            player_poisin = player_poisin + damage_tot -15

        #Call Damage Function Robot
        RoboHealth = health_loss(damage_tot,type,RoboHealth,player_poisin,"Robot")

        #Tell User How Much Health Left
        print(f"The Robot has {RoboHealth} health left")

        #Exit Loop if Player Wins
        if RoboHealth <= 0:
            break
        #Robot Choses Random Damage Type between 1 and 2
        robotype = random.randint(1,2)
         # Make Random Lists for Damage
        damage1, damage2 = create_damage_list(robotype)

        #Damage Function using Dot Product of List
        damage_tot = calc_damage(damage1,damage2)

        #Check Poisin Robot, and add
        if robotype == 2 and damage_tot > 15:
            robot_poisin = robot_poisin + damage_tot -15
            print(f"The Robot poisins you with 15+ damage!")

        #Call Damage Function Player
        PlayerHealth = health_loss(damage_tot,robotype,PlayerHealth,robot_poisin,"Player")
        print(f"You Have {PlayerHealth} health left")
    choice_win = robot_death()
    return choice_win
    
def main():
    print("main")



if __name__ == "__main__":
    main()