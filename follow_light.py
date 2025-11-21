import time
import math
from game_over import player_death
from finish_scentence import startscentence_game



def main():
    return

def try_light_max(curr_distance,max_distance):
    if (curr_distance > max_distance):
        print(f"The Light reached a distance of {curr_distance} which is a new best!")
        return curr_distance, curr_distance
    else:
        print(f"The Light reached a distance of {curr_distance}")
        return curr_distance, max_distance


def calc_range_height_tot(angle_launch):
    range_launch = ((10**2)*(math.sin(2*math.radians(angle_launch))))/9.8      #Calculate total x and y distance traveled and solve for total distance (using projectile motion!)
    height_launch = ((10**2)*((math.sin(math.radians(angle_launch)))**2))/(2*9.8)
    tot_launch = range_launch + height_launch
    return tot_launch
def light_game():
    with open("follow_light.txt",'r') as light_text:
        LengthLineReading = 55 #StartWithAverage 55 charecters /18 reading time Seconds
        for line in light_text:
            time.sleep(LengthLineReading/18)
            print(line.rstrip('\n'))
            LengthLineReading = len(line)

    tries_game = 6 #Allow the user 5 attempts (starting from 1)
    max_distance = 0.0  # Create variables for distance
    curr_distance = 0.0


    for i in range (1,tries_game): #Loop Through 5 games
        input_taken = False
        while input_taken == False:  #Loop Through and make sure input is correct
            angle_chosen = input(f"Select Angle {i}:  ")
            if angle_chosen.isdigit():
                if int(angle_chosen) <= 90 and int(angle_chosen) >= 0:
                    angle_chosen = int(angle_chosen)
                    input_taken = True
                else:
                    print("Please Enter a value between 0 - 90 degrees")
            else:
                print("Please enter a valid number")


        curr_distance = calc_range_height_tot(angle_chosen)
        curr_distance, max_distance = try_light_max(curr_distance, max_distance)


    if max_distance > 13.0: #Check Score and either keep player moving along, or end game for player
        print("You beat the distance of 13, congrats thats 5 points!")
        startscentence_game()
    else:
        print("You did not beat a distance of 13, sorry thats the game over")
        player_death()






if __name__ == "__main__":
    main()