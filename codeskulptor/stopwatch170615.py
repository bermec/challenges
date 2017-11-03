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
x = 0
y = 0
t = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    return str(t//600) + ":" + str(100 + (t//10%60))[-2:] + "." + str(t%10)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global x, y
    if timer.is_running():
        timer.stop()
        if t % 10 == 0:
            y += 1
            x += 1
        else:
            y += 1

def reset():
    global t, x, y
    timer.stop()
    t = 0
    x = 0
    y = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1
    
# define draw handler
def draw_handler(canvas):
    global x, y
    canvas.draw_text(str(x) + '/' + str(y), (200, 30), 20, 'Green')
    canvas.draw_text(format(t), (100,100), 40, "Yellow")
    
    
# create frame
frame = simplegui.create_frame("**Stopwatch, stop on whole second to gain a point!**", width, height)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric
