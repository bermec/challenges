# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True

import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PAD1_X_POS = HALF_PAD_WIDTH # center of paddle becasue the code uses draw_polygon
PAD2_X_POS = WIDTH - HALF_PAD_WIDTH# center of paddle becasue the code uses draw_polygon


# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [1, 1]
    #ball_vel = [random.randrange(120, 240), random.randrange(60, 180)]
    if right == False:
        ball_vel[0] *= -1
    return ball_pos, ball_vel

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(True)
    paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT # top position of paddle
    paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT # top position of paddle
    paddle1_vel = 0.0
    paddle2_vel = 0.0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen

        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([(HALF_PAD_WIDTH, paddle1_pos),         (HALF_PAD_WIDTH, paddle1_pos+PAD_HEIGHT)],         PAD_WIDTH, "White")
    c.draw_polygon([(WIDTH - HALF_PAD_WIDTH, paddle2_pos), (WIDTH - HALF_PAD_WIDTH, paddle2_pos+PAD_HEIGHT)], PAD_WIDTH, "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White")
    
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH or ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        ball_vel[0] *= -1
    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] *= -1        
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()


