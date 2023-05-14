#MEMORY GAME 

import simplegui as sg 
import random as rn


deck_list = range(0,8) + range(0,8)

#function used every time the game starts or restarts 
def new_game() :
    global state , count_turn , exposed , deck_list 
    rn.shuffle(deck_list)
    exposed = []
    for i in range(16):
        exposed.append(False)
    state = 0 
    count_turn = 0 
    
#function to handle the mouseclick 
def mouseclick(position):
    global state , count_turn , click1, click2
    card_num = position[0]/50
    
    #funvtion that checks if the click is in a card 
    def is_valid_click():
        for i in range(16):
            if position[0] <= (i+1) * 50 and position[0] >= i*50 and exposed[i] == False:
                return True
    
    #function that find which card to show 
    def expose():         
        for i in range(16):
            if position[0] <= (i+1) * 50 and position[0] >= i*50:
                exposed[i] = True
                return i
    
    if is_valid_click():
        #the 3 different states of the game 
        #state 0
        if state == 0:
            state = 1
            click1 = expose()
        #state 1 
        elif state == 1:
            state = 2
            count_turn += 1
            label.set_text("Turns = " + str(count_turn))
            click2 = expose()    
        #state 2 
        else:
            state = 1 
            #check if the two shown cards are the same 
            if deck_list[click1] != deck_list[click2]:
                exposed[click1] = False
                exposed[click2] = False
            click1 = expose()
  
#function to handle the canvas 
def draw_handler(canvas):
    global deck_list, exposed 
    for i in range(16) :
        if exposed[i]  :
            canvas.draw_text(str(deck_list[i]), ((i+1) * 50 - 30, 50), 20, "Red")
        else: 
            canvas.draw_polygon([((i)*50,0), ((i)*50, 100),((i+1)*50, 100), ((i+1)*50, 0)], 1, "Black", "Green")


frame = sg.create_frame("MEMORY",800,100)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouseclick)
label = frame.add_label("Turns = 0")
restart = frame.add_button("Restart",new_game)

new_game()
frame.start()
