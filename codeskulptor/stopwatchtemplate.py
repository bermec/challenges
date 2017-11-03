# template for "Stopwatch: The Game"
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

# define global variables
width = 300
height = 200
interval = 100
t = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    return str(t//600) + ":" + str(100 + (t//10%60))[-2:] + "." + str(t%10)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    timer.stop()

def reset():
    global t
    timer.stop()
    t = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), (100,100), 24, "Yellow")
    
# create frame
frame = simplegui.create_frame("clock", width, height)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)
frame.add_button('Exit', exit)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
