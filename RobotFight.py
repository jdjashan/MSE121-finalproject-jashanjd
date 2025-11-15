import random


def RobotDeath():
    print("GoodJob")
def HealthLoss(Damage,Type,Health,Poisin):
    if Type == "Basic":
        if (Health - Damage - Poisin/5) <=0:
            RobotDeath()
            return 0
        else: 
            return (Health - Damage - Poisin/5)
    elif Type == "Poisin":
        if Damage >= 15:
            if (Health - 15 - Poisin/5) <=0:
             RobotDeath()
             return 0
            else: 
                return (Health - 15 - Poisin/5)
        else: 
            if (Health - Damage - Poisin/5) <=0:
                    RobotDeath()
                    return 0
            else:
                return (Health - Damage - Poisin/5)
    elif Type == "Chance":
        RobotDeath()
        return 0



def main():
    RoboHealth = 50
    PlayerHealth = 50
    while (RoboHealth != 0 or PlayerHealth != 0):
        #Player Choice
        print("Type 1 for Basic Attack")
        print("Type 2 for Poisin Attack")
        print("Type 3 for a Chance Attack")

        #Damage Function using Dot Product of List



        #Check Poisin, and add

        #Call Damage Function






if __name__ == "__main__":
    main()