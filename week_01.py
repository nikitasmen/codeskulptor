# RLPS GAME 

import random as rn 

#function to convert a name to number 
def name_to_number(name):
    if name == "rock":
        num = 0
    elif name == "Spock":   
        num = 1
    elif name == "paper":
        num = 2 
    elif name == "lizard":
        num = 3 
    else:
        num = 4 
    return num 

#funtion to convert a number to name 
def number_to_name(number):
    if number == 0 :
        name = "rock"
    elif number == 1 :
        name = "Spock"
    elif number == 2 :
        name = "paper"
    elif number == 3 :
        name = "lizard"
    else:
        name = "scissors"
    return name 


def rpsls():

    #players choise considering that the input is correct 
    player_choise = ""
    player_choise = input()
    player_number = name_to_number(player_choise)
    print "Player chooses ",player_choise 
    
    #computer's choise is random using the function random.randint, from the "random" library 
    comp_number = rn.randint(0,4)    
    comp_name = number_to_name(comp_number)
    print "Computer chooses ",comp_name

    #determination of the winner of the game 
    if comp_number == player_number:
        print "Player and computer tie!"
    elif comp_number == 0 :
        if player_number == 3 or player_number == 4:
            print "Computer wins!"
        else: 
            print "Player wins!" 
    elif comp_number == 1 :
        if player_number == 0 or player_number == 4:
            print "Computer wins!"
        else:
            print "Player wins!"
    elif comp_number == 2 :
        if player_number == 0 or player_number == 1:
            print "Computer wins!"
        else:
            print "Player wins!"
    elif comp_number == 3 :
        if player_number == 1 or player_number == 2:
            print "Computer wins!"
        else:
            print "Player wins!"
    elif comp_number == 4 :
        if player_number == 2 or player_number == 3:
            print "Computer wins!"
        else:
            print "Player wins!"

    #empty line to indicate the end of the game 
    print("\n")



if __name__=='__main__':
    while True :
        rpsls()