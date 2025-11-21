import time
import sys
def player_escapes():
    with open("player_name.txt","r") as name_file:
        name = name_file.read()
        print(f"Wow, {name} journey comes to an end here")
        time.sleep(2)
        print(f"Master Jeff: 'I am proud of you {name}, you really did escape the terminal")
        time.sleep(3)
        print("Master Jeff: 'More than escaping the terminal, you learnt alot about life, oppurtunity, forggeting hurtful things from your past, and appreciating what you have in your moment.")
        time.sleep(3)
        print("Master Jeff: 'I hope to see you taking these new lessons on with your life outside of the terminal")
        time.sleep(3)
        print("Thank you player, and just remember, when all hope seems lost, there are always people around you who love you for who you are, so stay true to yourself...")
        time.sleep(2)
    sys.exit()

def main():
    return



if __name__ == "__main__":
    main()