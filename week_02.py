

import simplegui as sg 
import random as rd

secret_number = rd.randrange(0,100)
game_range = 100
chance = 7

#function to start a new game 
def new_game():
    global secret_number , chance
    secret_number = rd.randrange(0,game_range)
    if game_range == 100:
        chance = 7 
    else:
        chance = 10

        
#function to change the range of the secret number to 1000
def game_100():
    global game_range
    game_range = 100
    new_game()
    print "New game started"

#function to change the range of the secret number to 1000
def game_1000():
    global game_range 
    game_range = 1000
    new_game()
    print "New game started"
    
    
#main game function     
def input_guess(guess):
    global chance 
    #convert the input from str to int 
    guess = int(guess)
    print "Guess was ",guess
    #guess higher than the secret number 
    if guess>secret_number :
        print "Lower"
        chance -= 1
        print "Chances left: ", chance
    #guess lower than the secret number    
    elif guess<secret_number :
        print "Higher"
        chance -= 1
        print "Chances left: ", chance
    #guess equal to the secret number and starts a new game 
    else:
        print "Correct"
        new_game()
        print""
        print "New game started"
    #player is out of chances so the game will restart 
    if chance == 0 :
        print "You run out of chances"
        new_game()

#create the game's frame 
frame = sg.create_frame('Guess the number game',300,300)
#text input box for the guesses
guess = frame.add_input('input_guess',input_guess,50)
#button to restart the game 
new_game_button = frame.add_button("new_game",new_game)
#button to start a new game where the secret number is in [0,100)
new_game_100 = frame.add_button("Range :0-100",game_100)
#button to start a new game where the secret number is in [0,1000)
new_game_1000 = frame.add_button("Range :0-1000",game_1000)



frame.start()