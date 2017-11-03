__author__ = 'rog'
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
WIDTH = 40
SPACER= 10

def make_numbers():
    card_values = []
    while len(card_values) < 16:
        x = random.randrange(1, 9)
        if card_values.count(x) != 2:
            card_values.append(x)
    return card_values

data = []
def new_game():
    data.clear()
    xpos = SPACER
    for item_id, item in enumerate(make_numbers()):
        xpos += WIDTH
        data.append([item_id, item, True, False, xpos - WIDTH, xpos])
        xpos += SPACER
new_game()

def check_list(l):
    for item in set(l):
        if l.count(item) >= 2:
            return True
    return False

def two_card_check():
    cards = []
    for item in data:
        if not item[2] and not item[3]:
            cards.append(item[0])
    if len(cards) >= 2:
        print([data[x][1] for x in cards])
        # Check to see if won
        if check_list([data[x][1] for x in cards]) == 1:
            for item in cards:
                data[item][3] = True
        # Rehide failed cards
        for item in cards:
            if not data[item][3]:
                data[item][2] = True

def click(pos):
    for item in data:
        if pos[0] >= item[4] and pos[0] <= item[5]:
            break
    two_card_check()
    data[item[0]][2] = False
    print(item, data)
# cards are logically 50x100 pixels in size
def draw(canvas):
    xpos = SPACER
    for item in data:
        if item[2]:
            canvas.draw_polygon([(xpos, 20), (xpos + WIDTH, 20),
                                 (xpos + WIDTH, 120), (xpos, 120)],
                                1, u'Green', u'Red')
        else:
            canvas.draw_text(item[1],(xpos + 10,80), 20, u'White')
        xpos += WIDTH + SPACER
frame = simpleguitk.create_frame(u"Memory", 810, 100)
frame.add_button(u"Restart", new_game)
label = frame.add_label(u"Turns = 0")
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

