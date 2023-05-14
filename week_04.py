#Pong game 
import simplegui as sg
import random as rn


width  = 600
height = 400       
ball_radious = 20
pad_width = 8
pad_height = 80
half_pad_width = 4
half_pad_height  = 40
left = False
right  = True

paddle1_vel = 0
paddle2_vel = 0

velocity_increase = 1.1


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [width/ 2, height /2]
    ball_vel = [rn.randrange(120, 240), rn.randrange(60,180)]
    if direction == right:
        ball_vel[1] = -ball_vel[1]
    if direction == left:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2  
    score1 = 0
    score2 = 0
    paddle1_pos = height / 2
    paddle2_pos = height / 2
    spawn_ball(rn.choice([left,right]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "White")
        
   
   
    if ball_pos[1] <= ball_radious or ball_pos[1] >=height-ball_radious:  
        ball_vel[1] = -ball_vel[1]
        
    if ball_pos[0]-8 <= ball_radious:  
        
        if paddle1_pos - half_pad_height <= ball_pos[1]<=paddle1_pos + half_pad_height:  
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * velocity_increase
            ball_vel[1] = ball_vel[1] * velocity_increase
        
        else:
            spawn_ball(right)
            score2 += 1
            
    if ball_pos[0] >= width - ball_radious - pad_width:
        
        if paddle2_pos - half_pad_height <= ball_pos[1] <= paddle2_pos + half_pad_height:
                ball_vel[0] = -ball_vel[0]
        else:
            spawn_ball(left)
            score1 += 1
            
        
    ball_pos[0] += ball_vel[0]/100
    ball_pos[1] += ball_vel[1]/100
    # draw ball
    canvas.draw_circle(ball_pos, ball_radious, 2, "Red", "White")
    
    # update paddle's vertical positionradious, keep paddle on the screen
    if half_pad_height <= paddle1_pos + paddle1_vel <= height - half_pad_height:
        paddle1_pos += paddle1_vel
    if half_pad_height <= paddle2_pos + paddle2_vel <= height - half_pad_height:
        paddle2_pos += paddle2_vel
    
    canvas.draw_line([half_pad_width, paddle1_pos + half_pad_height], [half_pad_width, paddle1_pos - half_pad_height], pad_width, "White")   
    canvas.draw_line([width - half_pad_width, paddle2_pos + half_pad_height], [width - half_pad_width, paddle2_pos - half_pad_height], pad_width, "White")
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1) + "     " + str(score2), (width / 2 - 36, 40), 30, "Green")      
    
#keyboard event handlers
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == sg.KEY_MAP['s']:  
        paddle1_vel = 3  
    elif key == sg.KEY_MAP['w']:  
        paddle1_vel = -3  
    elif key == sg.KEY_MAP['up']:  
        paddle2_vel = -3  
    elif key == sg.KEY_MAP['down']:  
        paddle2_vel = 3 
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == sg.KEY_MAP['s']:  
        paddle1_vel = 0  
    elif key == sg.KEY_MAP['w']:  
        paddle1_vel = 0
    elif key == sg.KEY_MAP['up']:  
        paddle2_vel = 0 
    elif key == sg.KEY_MAP['down']:  
        paddle2_vel = 0
    

frame = sg.create_frame("Pong Game", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_button = frame.add_button('Restart', new_game, 100)


new_game()
frame.start()
    