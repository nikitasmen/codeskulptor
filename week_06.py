#Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
actions = "Hit or Stand?"
first_game = True
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self._cards = []	# create Hand object

    def __str__(self):
        self.ans = ""	# return a string representation of a hand
        for i in range(len(self._cards)):
            self.ans += str(self._cards[i]) + " "
        return self.ans
    
    def add_card(self, card):
        self._cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.value = 0
        for card in self._cards:
            self.value += VALUES[card.get_rank()]
        for card in self._cards:
            if card.get_rank() == 'A' and self.value + 10 <= 21:
                self.value += 10
        return self.value
    
    def draw(self, canvas, pos):
        for i in range(len(self._cards)): # draw a hand on the canvas, use the draw method for cards
            pos[0] =50 + 100*i
            self._cards[i].draw(canvas,pos)
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [ Card(i,j) for i in SUITS for j in RANKS ]	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        self.card = self.deck.pop(0)# deal a card object from the deck
        return self.card
    
    def __str__(self):
        self.str_deck = "" # return a string representing the deck
        for i in range(len(self.deck)):
            self.str_deck += str(self.deck[i]) + " "
        return self.str_deck        


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score, outcome, actions

    # your code goes here
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    print "Player has %s" % player_hand
    print "Dealer has %s" % dealer_hand
    if in_play:
        score -= 1
    in_play = True
    outcome = ""
    actions = "Hit or Stand?"
    

def hit():
    global player_hand, deck, in_play, outcome, actions
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())# replace with your code below
            print player_hand.get_value()
            if player_hand.get_value() > 21:
                outcome = "You have busted"
                actions = "New Deal?"
               
            else:
                print player_hand
        
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global player_hand, dealer_hand, score, outcome, actions, in_play 
    
    if in_play:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
        
        if dealer_hand.get_value() == 21:
            outcome = "Dealer Wins!"
            actions = "New Deal?"
            score -= 1
        elif dealer_hand.get_value() > 21:
            outcome = "Dealer is busted! You win"
            actions = "New Deal?"
            score += 1
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                outcome = "You Win!"
                actions = "New Deal?"
                score += 1
            else:
                outcome = "Dealer Wins!"
                actions = "New Deal?"
                score -= 1
    
    print dealer_hand
    print player_hand.get_value()
    print dealer_hand.get_value()
    in_play = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

    
def draw(canvas):
   
    player_hand.draw(canvas,[50, 400])
    dealer_hand.draw(canvas,[50, 150])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [86.5, 200], CARD_BACK_SIZE)
    canvas.draw_text("Blackjack",(70,50), 25, 'Black', 'serif')
    canvas.draw_text(outcome, (50, 100), 30, 'Red')
    canvas.draw_text(actions,(400,100),20,'Black')
    canvas.draw_text("score:" + " " + str(score), (500,50), 25, 'Black') 
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


deal()
frame.start()

