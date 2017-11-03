import simpleguitk
clock = 0
milli = 0
sec = 0
min = 0

x = 7
y = 8

# draw handler
def draw_handler(canvas):
    global x, y
    canvas.draw_text(str(x) + '/' + str(y), (200,30), 20, 'Green')
    canvas.draw_text('0.01', (110,110), 40, 'Red')


    

def start():
    timer.start()

def stop():
    timer.stop()


# create frame
frame = simpleguitk.create_frame("test",300,200)
frame.set_draw_handler(draw_handler)
frame.start()
