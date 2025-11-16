
import time
from Choices import StartGame

    

def FirstChoice():
    AnimationSpace = 10
    AnimationTime = 3
    print("You: 'Where Am I, What Is This Place' ")
    time.sleep(AnimationTime)
    print("You: 'Why Is it So Dark...' ")
    time.sleep(AnimationTime)
    print("Random: 'Welcome Foreigner, I Invite You to The Terminal. I am Master Jeff!' ")
    time.sleep(AnimationTime)
    print("You: 'Wha, What is A Terminal' ")
    time.sleep(AnimationTime)
    print("Master Jeff: 'Heh, A Terminal is like the body of a human, its a place for proggramers to run code, commands, debug, and manage files!' ")
    time.sleep(AnimationTime+2)
    print("You: 'Ew. Bugs, where?' ")
    time.sleep(AnimationTime)
    print("Master Jeff: 'Ignorance is Bliss isnt it, Look Son, You Dont Have Much Time to Get Out of Here before your stuck Forever.' ")
    time.sleep(AnimationTime+3)
    print("You: 'FOREVER. Nuh Uh, not happening. How Do I Leave The Teermiineeeal'")
    time.sleep(AnimationTime)
    print("Master Jeff: 'Well, to escape the Ter-Min-Al, you can either collect 3 items around the terminal and bring them back to me' (Click f + Enter at any choice to look at item list)" )
    time.sleep(AnimationTime+4)
    print("Master Jeff: 'OR, you can get 10 points by winning games allover, that should instantly teleport you back home" )
    time.sleep(AnimationTime+5)
    print("You: 'Ok, but its all black, where would I play or get your stuff'")
    time.sleep(AnimationTime+1)
    print("Master Jeff: 'Thats For Your to DECIDE son, Goodbye, Ill be seeing You Soon" )
    time.sleep(AnimationTime+3)
    print(".  .  .  .  .  .  .  .")
    time.sleep(AnimationTime-2)
    print(" .  .  .  .  .  .  .  .")
    time.sleep(AnimationTime-2)
    print("  .  .  .  .  .  .  .  .")
    time.sleep(AnimationTime-2)
    print(" .  .  .  .  .  .  .  .")
    time.sleep(AnimationTime-2)
    print(".  .  .  .  .  .  .  .")
    time.sleep(AnimationTime)
    print("First Choice:")
    print(" Type 1 to Walk In the Same Direction As Master Jeff")
    print(" Type 2 to Walk In the Opposite Direction As Master Jeff")
    print(" Type 3 to NOT Walk and Let Someone else stumble upon you")
    input()


def main():
    StartGame()
    












if __name__ == "__main__":
    main()