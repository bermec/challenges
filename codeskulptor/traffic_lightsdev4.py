# Timers
# Traffic lights

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True


# Global Variables

canvas_width = 600
canvas_height = 600
message = "Hello!"
displayed = True
timer_interval = 1000  # In milliseconds (1000 ms = 1 s)
red = True
amber = False
green = False
stop = False
cross = -1
state = True
crossing = False
flag = False

# Event Handlers

def start():
    global red

    timer.start()
    frame.start()
    red = True

def stop():
    global red
    global amber
    global green
    red = True
    amber = False
    green = False
    timer.stop()
    frame.stop()


def reset():
    global red
    global amber
    global green
    red = True
    amber = False
    green = False
    frame.start()

def cross_func():
    global cross
    cross = 1


def colors():
    global state
    if state == True:
        colour = 'Red'
    else:
        state = False
        colour = 'Green'
    return colour

def flash():
    global state
    state = not state
    return state


# Switches whether or not the text is visible
# Note that it does not have any parameters
def timer_handler():
    global red
    global amber
    global green
    global cross
    global state
    global flag

    print('line92 (handler): ', 'state ',  state, 't ', cross)


    if cross > 0 and flag == True:
    #if flag:
        print('flag = ', flag)
        cross += 1
    if 0 <= cross <= 10:
        state = False
        print('0 to 10')
    elif 11 <= cross <= 14:
        state = flash()
        print('11 to 14')

    else:
        cross == 15
        cross = -1
        state = True
        print(state, cross,'t= ', cross)
        print(red, amber, green, cross)


        print('line 97 (+=) ', cross)
    if red and not amber and not green:
        flag = True
        if cross > -1 and cross < 15:
            return
        else:
            cross = -1
        red = True
        amber = True
        green = False
    elif (amber and red) and not green:
        green = True
        red = False
        amber = False
        flag = False
    elif green and not red and not amber:
        amber = True
        red = False
        green = False
        flag = False
    elif amber and not red and not green:
        red = True
        amber = False
        green = False
        flag = False


    print('line120 (handler): ', state, 't= ', cross)





def draw(canvas):
    global red
    global amber
    global green
    color = colors()

    if red:
        canvas.draw_circle((200, 130), 40, 2, "Aqua", "Red")
    if amber:
        canvas.draw_circle((200, 260), 40, 2, "Aqua", "Orange")
    if green:
        canvas.draw_circle((200, 390), 40, 2, "Aqua", "Green")
    canvas.draw_polyline([(100, 50), (300, 50), (300, 450), (100, 450), (100, 50)], 5, 'Red')
    canvas.draw_polyline([(190,50), (190, 40), (210, 40), (210, 50)], 5, 'Red')
    canvas.draw_polyline([(190,450), (190, 590), (210, 590), (210, 450)], 5, 'Red')
    canvas.draw_circle((400,100), 25, 2, color, color)
    canvas.draw_polygon([(380, 120),(420, 120),(430, 230),(390,230)], 2, color, color)
    canvas.draw_polygon([(420, 230),(390, 230),(330, 330),(360,340)], 2, color, color)
    canvas.draw_polygon([(430, 230),(400, 230),(440, 360),(470,350)], 2, color, color)
    canvas.draw_polygon([(420, 120),(400, 120),(470, 230)], 2, color, color)
    canvas.draw_polygon([(380, 120),(420, 120),(320, 230)], 2, color, color)
    canvas.draw_polygon([(340, 330),(340, 315),(305, 320)], 2, color, color)
    canvas.draw_polygon([(450, 355),(450, 335),(415, 365)], 2, color, color)
# Frame

frame = simplegui.create_frame("Pedestrian Crossing", canvas_width, canvas_height)

# Register Event Handlers

frame.set_draw_handler(draw)


# Creates a timer. Check the docs for more details.
timer = simplegui.create_timer(timer_interval, timer_handler)
frame.add_button("Cross", cross_func)
startButton = frame.add_button("Start", start)
stopButton = frame.add_button("Stop", stop)
resetButton = frame.add_button("Reset", reset)

# Remember to start the timer as well as and BEFORE the frame
start()

