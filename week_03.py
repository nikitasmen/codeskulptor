"""StopWatch: The Game"""

import simplegui as sg 


interval = 100
time = 0 
d = 0
c = 0
b = 0 
a = 0 
stops = 0
score = 0 

#function that adds time 
def timer_handler():
    global time 
    time = int(time)
    time +=1

#function that starts the timer 
def start():
    timer.start()

#function that stops the timer and adds plus 1  if already stopped in var stops , and adds plus 1 if stop in correct time add one at score
def stop():
    global stops,score
    stops = int(stops)
    score = int(score)
    if timer.is_running():
        stops +=1
        if time%10 == 0 :
            score +=1
    timer.stop()
    
#function that sets time score and number of stops to 0    
def reset():
    global time,stops,score
    timer.stop()
    time = 0 
    stops = 0 
    score = 0 
    
#function that draws time,score and number of stops at the canvas 
def draw_handler(canvas):
    global time,stops,score
    timer =format(time)
    stops = str(stops)
    score = str(score)
    canvas.draw_text(score,[125,50],50,"Green")
    canvas.draw_text("/",[150,50],50,"Green")
    canvas.draw_text(stops,[160,50],50,"Green")
    canvas.draw_text(timer,[40,120],50,"Red")

#function that converts time from int to char "0:00.0"
def format(t):
    global d,c,b,a
    a = (t/600)
    b = (t/100)%6
    c = (t/10)%10
    d = t%10
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    timer = str(a)+":"+str(b)+str(c)+"."+str(d)
    return timer


frame = sg.create_frame("Stopwatch: The Game",200,200)
start_timer_button = frame.add_button("start",start)
stop_timer_button = frame.add_button("Stop",stop)
reset_timer_button = frame.add_button("Reset timer",reset)

timer = sg.create_timer(interval,timer_handler)

frame.set_draw_handler(draw_handler)



frame.start()

