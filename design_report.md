1) 

On a basis level this program is made to be fun, interactive, and give the user an immersive experience. It contains many different paths, mini games, characters, and interesting storylines. Though when examining the game deeper, you will find it actually teaches the user very powerful life skills and lessons. The purpose of this game is to bestow knowledge that I have come to accept in the past couple years, using quotes, games, and character dialogue. There are many lessons ranging from the power of friendship and love to appreciating the time you have on earth. At the end of the day, I hope the user comes out of the program with some thoughts in their head, hopefully making them realise something they didn't appreciate previously.  

 

2) 

With a program such as this, you find that there is a lot of user input and output to the terminal. I managed to split every decision into functions across 10 files. These functions are very much connected to the main file Game.py and Choice.py. 

In Choice.py you find the function:  FirstChoiceMade(choice) 

Which first takes the inputs and figures out which file to read from:  

if Choice == 1: 

        Storyline = open("FollowJeff.txt",'r') 

    elif Choice == 2: 

        Storyline = open("OppositeJeff.txt",'r') 

    elif Choice == 3: 

        Storyline = open("StayStill.txt",'r') 

Once the file is chosen, the for line in Storyline feature is used to loop through the lines and read the file out to the user: 

 

for line in Storyline: 

        ReadLine = line 

        if ReadLine == "S": 

            Storyline.close() 

            make_choice() 

        elif ReadLine == "C": 

            Storyline.close() 

            is_chosen = False 

            while is_chosen == False: 

                choice_opp = input() 

                if choice_opp == "1" or choice_opp =="2" or choice_opp =="3": 

                    choice_opp = int(choice_opp) 

                    is_chosen = True 

                else: 

                    print("Choose a valid option please") 

            if choice_opp == 1: 

                light_game() 

                Storyline.close() 

            elif choice_opp == 2: 

                Storyline.close() 

                connect_people() 

            elif choice_opp == 3: 

                Storyline.close()                

                print("Probably not the best idea, screaming into a void of nothingness, hoping for some result") 

                time.sleep(3) 

                print("Those sounds of people are gone, but you hear a loud screeching noise approaching you") 

                time.sleep(3) 

                print("and as it gets locer you sit there and realise your fate") 

                time.sleep(1.5) 

                print("Goodbye, fair soldier") 

                time.sleep(1) 

                player_death() 

                 

        elif ReadLine.strip() == "G": 

            Storyline.close() 

            robot_win_choice(Rmain()) 

        else:  

            time.sleep(LengthLineReading/18) 

            print(ReadLine.rstrip('\n')) 

            LengthLineReading = len(line) # Make Reading Length Based on line 

The Code above also shows, how at the end of the file I put a character to check which type of file it is, “C” for Choice, “G” for Robot Game, “S” for Stay Still. 

It also shows how i use time(imported) to perform the reading on time intervals, based on the length of the previous line (the line the user is current reading) 

Then based off the file, it either takes another user input as a choice or takes the user straight to a function in another file. 

This is how most of the code in the program works. It is taking in input reading files, then taking the user to a specified place or calling a function from another file. The other functions are shorter, because they don't open multiple files, only one, this was only for the first choice. 

This stopped a huge chunk of code in single functions and also stopped having a single file having 10-20 long functions and rather separated across many files, that make it easier for another software developer to enter and see exactly what I had in mind! 

The functions that are different are the ones for the games, which are ones that have actual logic. Therefore, a lot of functions for the games were extracted from inputs so they could be pytested.  

For example, when making the robot game, I created separate functions called calc_damage and create_damage_lists. These do not take user input and therefore can be tested 

Here is calc_damage: 

    total_dmg = 0 

    for i in range (len(dmg1)): 

        total_dmg = total_dmg + dmg1[i-1]*dmg2[i-1] 

    return total_dmg 

Very Simple, yet it takes in two parameters dmg1 and dmg2, which are created by create_damage_lists: 

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

This function takes in type, which is a user input, though it takes it as a parameter so this can be tested. That is the reason it is not within the function. 

With the type it creates two lists, with random ints from 1-6. And returns the two. These are then shared with calc_damage. Which dot products the two lists to calculate total damage. 

There was a total of 4 tests written for these testing the types and outputs. 

 

Another example is: 

Check_answer(guess,correct_guess) 

 

 

This simple function is separated from the functions with inputs so it can be pytested, and it very simply takes an answer and the correct answer. It checks is your answer is equal to the correct answer, if so, it returns 1 otherwise it returns 0: 

 

def check_answer(guess,correct_guess): #function that checks answer 

    if guess == correct_guess: 

        return(1) 

    else: 

        return(0) 

 

3) 

There were countless challenges I faced whilst making Stuck In The Terminal: A Choose Your Own Adventure Story. Hilariously enough, it was the coding that created many challenges, but it was the substance of the program that I am most proud of.  

I struggled many times, but here are some highlights that I think we're cool to have figured out: 

Figuring out the poison damage, trying to carry poison across multiple rounds, and figuring out how to do a fifth of the total poison damage each time.  

To solve this, I created both a poison variable in the damage function and the original function. When the player/robot shoots a poison shot, their poison gets updated for whatever is over 15 and then is called to the damage function. The poison counter is always updated after every shot in the main function, and its damage is done in the damage function! 

 

I had difficulty creating a proper amount of time to sleep after every scentence, especially when one sentence was 1 word, and the other was 20. I could set a base time, but then the user would be sitting for way too long for the shorter sentences or not have enough time to read the longer sentences.  

 

To solve this, what I did was had a variable called LengthLineReading which contains the amount of time to sleep. This variable is updated as the code loops through the lines of the file, it reads the length of the line then it sleeps the length divided by 18. Some important information: 

It reads the length of the line after printing it, then sleeps before printing the next line, making sure it waits for the line that was just printed and not the next one 

The length is divided by 18 because of some research on how many characters humans read per minute on average. Using that I found it was about a 18th – 20th of a second per character on average. 

When looking at the project as a whole, I'm actually the proudest at the concept of newfound learning. The number of quotes and lessons present in the story and games makes me feel as if the game is achieving something when being played.  Especially the quote game which featured one of my personal quotes that I made just through lessons I learnt along the way in life!  

 

4) 

To Improve it is extremely important to recognize that there is so much that can be done to make this game even better, though in a short time, I feel I was able to complete the needed aspects of the game well! All in all, I do recognize that many of the games feel very basic, and a little gimmicky, especially since some have no way to lose and only serve as a lesson. I would love to try to enhance the games in the future, and add more skill-based factors to make the games more enjoyable. 

I would say the major areas to improve are: 

The length of some of the paths 

The complexity and enjoyability of the minigames 

The lack of characters in the story 

More customizability for the user/player 

 

5) 

This section is probably the most important one when relating to my program. Throughout this project, in the attempt of teaching the player something about life, I gained some new knowledge myself. Really just playing through my game I was just hit with nostalgia because I tried making this game on lessons from the past that I have come to accept.  

These lessons really helped me understand a little better. See before they just existed in my mind, but when putting them on a canvas, I truly got to see what had previously only been a feeling.  

On top of that, whilst making the different games I had to do a lot of research finding many new quotes such as:  

"Hope is being able to see that there is light despite all of the darkness" 

And 

"Some people are so afraid to die that they never begin to live.” 

 

Both these quotes are excellent at putting forth the fact that we only live once. That living in the moment and not letting the bad things, or not even trying, is never the way to live your life. That message really hit me hard... I feel as if it truly understands me, because right now I keep hitting myself with nostalgia from the past. 

On the coding side I also learnt a lot...  

From understanding imports from python's library like import time, and import sys 

Also, I tried a new type of development for many of the functions in my program called test driven development. This new type of development helped me create test cases, then slowly accomplish them whilst creating the functions for the game. 

 

In total, this project taught me a lot about not only code, but determination and time management. As well as some wisdom from Master Jeff along the way. My only question to you is, can you Escape The Terminal? 

 

 

 

 