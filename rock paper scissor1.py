from random import randint

def num_turns():
    while True:
        turns = input("Please enter the attempts we wish(between 1 to 5) to play the game: ")
        try:
            turns = int(turns)
            if 1<= turns <=5:
                print("We are gonna play the game for {} turns".format(turns))
                return turns
            else:
                print("{} is not a no between 1 and 5".format(turns))
        except ValueError:
            print("Entered {} is not a valid no for turns".format(turns))
        
            
attempts = num_turns()

def game_output(p1,p2):
    if p1 == "r" and p2 =="s":
        s1,s2 = 1,0
    elif p1 == "r" and p2 =="p":
        s1,s2= 0,1
    elif p1 == "p" and p2 =="r":
        s1,s2 = 1,0
    elif p1 == "p" and p2 =="s":
        s1,s2= 0,1
    elif p1 == "s" and p2 =="p":
        s1,s2 = 1,0
    elif p1 == "s" and p2 =="r":
        s1,s2 = 0,1
    else:
        s1,s2= 0,0
    return s1,s2

        

x = ["r", "p", "s"]
score1=[]
score2=[]
for i in range(1,attempts+1):
    computer = randint(1,3)
    while True:
        player_choice = input("For turn:%d, please enter your choice of 1-Rock, 2-Paper and 3-Scissor(only 1/2/3 is valid): " %i)
        try:
            player_choice = int(player_choice)
            if 1<= player_choice <=3:
                print("You have choosen %s" %x[player_choice-1])
                break
            else: print("Please enter no between 1 and 3 only")
        except ValueError:
            print("You havent entered a valid no between 1 and 3")
    print("Computer has choosen: %s" %x[computer-1])
    comp = x[computer-1]
    player = x[player_choice-1]
    output = game_output(comp,player)
    if output[0] > output[1]: print("Computer won this round")
    elif output[0] < output[1]: print("You won this round")
    else: print("its a tie, lets play again!")
    score1.append(output[0])
    score2.append(output[1])

print(score1)
print(score2)
sum_score_comp = sum(score1)
sum_score_player = sum(score2)

if sum_score_comp >= sum_score_player:
    print("You lost the game, Computer won")
else: print("Congrats! You have won the game")
    
    
            
                      

