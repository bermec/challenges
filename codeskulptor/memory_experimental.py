import simpleguitk as simplegui
import random


card_up =[]
card_paired = []
state = 1
turns = 0

def make_numbers():
    card_values = []
    while len(card_values) < 16:
        x = random.randrange(1, 9)
        if card_values.count(x) != 2:
            card_values.append(x)
    return card_values

# produce the data for all cards
data = []
for item_id, item in enumerate(make_numbers()):
    data.append([item_id, item, state])


# helper function to initialize globals
def new_game():
    global state, turns, data
    state = 1
    turns = 0
    label.set_text('Moves = ' + str(turns))


#card_up[] = cards showing - minus pairs
#
# define event handler for mouse click, draw
def click(pos):
    global data, card_up, turns, card_paired

    turns += 1
    label.set_text('Moves = ' + str(turns))

    # works out index of card
    card_index = pos[0] // 50

    # data of card clicked
    card_data = data[card_index]
    data[card_index][2] = 0
    print (card_data)
#---now have all info required -------------------------
    print(' 1.card_up b4 pairing: ',card_up)


    # first check for pairs
    if len(card_up) >= 2:
        print('2. card_up passed pairing check: ',card_up)
        #for item in card_up:
        print('pair process')
        if card_up[0][1] == card_up[1][1]:
             card_paired = card_up[:2] + card_paired
             card_up = []
    print('3. card_paired: ', card_paired,' card_up: ',card_up)
    # place card in card_up if non-paired
    ''' if card_data in card_paired:
        pass
    else:
        card_up.append(card_data)'''


    print('card_up b4 trim: ',card_up)

    if len(card_up) > 1:
        for item in card_up:
            if item in card_paired:
                del(item)
            else:
                card_up[0][2] = 1
                card_up[1][2] = 1

                card_up.pop(0)
                card_up.pop(0)

    card_up.append(card_data)

    print('card_up after trim: ',card_up)
    print()
    #===========================================================================

# cards are logically 50x100 pixels in size
def draw(canvas):
    global data
    for item in data:
        xpos = item[0] * 50
        if item[2]:
            canvas.draw_polygon([(xpos, 20), (xpos + 40, 20),
                                 (xpos + 40, 120), (xpos, 120)],
                                1, 'Green', 'Red')
        else:
            canvas.draw_text(str(item[1]),(xpos + 10,80), 20, 'White')


def restart():
    global data, card_up, card_paired
    for item in data:
        item[2] = 1
    turns = 0
    label.set_text('Moves = ' + str(turns))
    card_up = []
    card_paired = []

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", restart)
label = frame.add_label('Moves = 0')
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()