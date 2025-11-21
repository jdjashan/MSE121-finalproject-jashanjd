
import time
from Choices import StartGame



def main():
    
    with open("player_name.txt", "w") as name_file:
        print("Before the game begins, please enter your username player:")
        name_file.write(input())
    StartGame()
    












if __name__ == "__main__":
    main()