
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True


# Global Variables

canvas_width = 600
canvas_height = 600
state = True
interval = 100
timer_interval = 1000 # In milliseconds (1000 ms = 1 s)
cross = -1
count = 0


# Event Handlers

def start():
    timer.start()
    frame.start()


def stop():
    timer.stop()
    frame.stop()


def flash():
    global state
    state = not state
    return state


def colors():
    global state
    if state:
        colour = 'Red'
    else:
        state = False
        colour = 'Green'
    return colour


# crossing function
# cross = 1 starts the crossing timer
# cross = -1 switches off (in timer handler)
def cross_func():
    global cross
    global count
    for x in range(1, 10):
        count += x
    cross = 1


# Switches whether or not the text is visible
# Note that it does not have any parameters
def timer_handler():
    global cross
    global state
    blink = flash()


    if 0 <= cross <= 10:
        cross += 1
        state = False
    else:
        state = blink

    print(state, cross)
    if cross == 15:
       cross = -1



def draw(canvas):
    global state
    color = colors()

    canvas.draw_circle((400,100), 25, 2, color, color)
    canvas.draw_polygon([(380, 120),(420, 120),(430, 230),(390,230)], 2, color, color)
    canvas.draw_polygon([(420, 230),(390, 230),(330, 330),(360,340)], 2, color, color)
    canvas.draw_polygon([(430, 230),(400, 230),(440, 360),(470,350)], 2, color, color)
    canvas.draw_polygon([(420, 120),(400, 120),(470, 230)], 2, color, color)
    canvas.draw_polygon([(380, 120),(420, 120),(320, 230)], 2, color, color)
    canvas.draw_polygon([(340, 330),(340, 315),(305, 320)], 2, color, color)
    canvas.draw_polygon([(450, 355),(450, 335),(415, 365)], 2, color, color)
6
# Frame

frame = simplegui.create_frame("Pictures", canvas_width, canvas_height)

# Register Event Handlers

frame.set_draw_handler(draw)
frame.add_button("Cross", cross_func)
timer = simplegui.create_timer(timer_interval, timer_handler)
killButton = frame.add_button("Kill", stop)

# Remember to start the frame
start()
