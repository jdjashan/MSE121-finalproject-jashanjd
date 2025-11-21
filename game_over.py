import sys
import time
#Create Variable for reading time
def main():
    return

def player_death():
    time_read = 6
    print(" ")
    with open("player_name.txt","r") as name_file:
        name = name_file.read()
        print(" Now your soul rests lonely in the terminal")
        time.sleep(time_read)
        print("You have lost, and now your gone...")
        time.sleep(time_read)
        print("Just remember this simple quote:")
        time.sleep(time_read)
        print("Some people are so afraid to die that they never begin to live. - Henry Van Dyke")
        time.sleep(time_read)
        print(f"{name} Atleast you went out trying to escape the terminal, you were a nobel one")
        time.sleep(time_read)
        print(f"Master Jeff: 'I Salute You {name}, you did your best")
        time.sleep(time_read - 2)
        #exit the code
    sys.exit()

if __name__ == "__main__":
    main()