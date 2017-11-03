try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True






# Global Variables

canvas_width = 600
canvas_height = 600



# Event Handlers


def draw(canvas):
    canvas.draw_circle((300,100), 25, 2, 'Red', 'Red')
    canvas.draw_polygon([(280, 120),(320, 120),(330, 230),(290,230)], 2, 'Red', 'Red')
    canvas.draw_polygon([(320, 230),(290, 230),(230, 330),(260,340)], 2, 'Red', 'Red')
    canvas.draw_polygon([(330, 230),(300, 230),(340, 360),(370,350)], 2, 'Red', 'Red')
    canvas.draw_polygon([(320, 120),(300, 120),(370, 230)], 2, 'Red', 'Red')
    canvas.draw_polygon([(280, 120),(320, 120),(220, 230)], 2, 'Red', 'Red')
    canvas.draw_polygon([(240, 330),(240, 315),(205, 320)], 2, 'Red', 'Red')
    canvas.draw_polygon([(350, 355),(350, 335),(315, 365)], 2, 'Red', 'Red')
6
# Frame

frame = simplegui.create_frame("Pictures", canvas_width, canvas_height)

# Register Event Handlers

frame.set_draw_handler(draw)


# Remember to start the frame
frame.start()