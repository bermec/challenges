import simpleguitk
import math

# define global variables
interval = 10
position = [250,250]
mil_sec =0
sec = 0
mins = 0
t=0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

def format(t):
    global mil_sec
    global sec
    global mins
    sec_string = 0
    mins = 0
    mil_sec = (t %10)
    sec = (t-mil_sec )//10
    sec, mins = sec % 60 ,sec // 60
    if mil_sec > 9 :
        mil_sec = 0
        sec = sec + 1
        if( sec > 59):
            mins = mins + 1
            sec = sec - 60
            sec_string = str(sec)
            if len(str(sec)) == 1:
                sec_string = '0'+str(sec)
    return str(mins )+':'+str(sec_string) +'.'+str(mil_sec)

# define event handlers for buttons; “Start”, “Stop”, “Reset”

def start():
    timer.start()

def stop():
    timer.stop()

def reset():
    timer.stop()
    global t
    t = 0

def draw(canvas):
    canvas.draw_text(format(t),position,24,'White')
    canvas.draw_text('Scores',[350,60],20,'Red')

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t = t+1

# create frame
frame = simpleguitk.create_frame( 'Stop Watch Game ' , 500 , 500)
timer = simpleguitk.create_timer(interval,tick)

# register event handlers
frame.set_draw_handler(draw)
startButton = frame.add_button('Start', start)
stopButton = frame.add_button('Stop', stop)
resetButton = frame.add_button('Reset', reset)

# start timer and frame
frame.start()

 
