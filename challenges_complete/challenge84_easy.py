'''
Like many people who program, I got started doing this because
I wanted to learn how to make video games.

As a result, my first ever 'project' was also my first video game.
It involved a simple text adventure I called "The adventure of
the barren moor"

In "The adventure of the barren moor" the player is in the middle
of an infinite grey swamp. This grey swamp has few distinguishing
characteristics, other than the fact that it is large and infinite
and dreary. However, the player DOES have a magic compass that
tells the player how far away the next feature of interest is.

The player can go north,south,east,or west. In my original version
of the game, there was only one feature of interest, a treasure
chest at a random point in the world.

Here is an example playthrough of my old program:

You awaken to find yourself in a barren moor.  Try "look"
> look
Grey foggy clouds float oppressively close to you,
reflected in the murky grey water which reaches up your shins.
Some black plants barely poke out of the shallow water.
Try "north","south","east",or "west"
You notice a small watch-like device in your left hand.
It has hands like a watch, but the hands don't seem to tell time.

The dial reads '5m'

>north
The dial reads '4.472m'
>north
The dial reads '4.123m'
>n
The dial reads '4m'
>n
The dial reads '4.123m'
>south
The dial reads '4m'
>e
The dial reads '3m'
>e
The dial reads '2m'
>e
The dial reads '1m'
>e

You see a box sitting on the plain.   Its filled with treasure!
  You win!  The end.

The dial reads '0m'

Obviously, you do not have to use my flavor text, or my feature points.
As a matter of fact, its probably more interesting if you don't!

'''

import pygame
import random
import math
from pygame import mixer
import time

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
mixer.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (128, 128, 128)
display_size = 500
gameDisplay = pygame.display.set_mode((display_size, display_size))
pygame.display.set_caption(('Treasure'))
print('use arrow keys to move around')

gameExit = False

lead_x = display_size /2
lead_y = display_size /2
treasure_x = random.randint(3, (display_size / 2) - 3)
treasure_y = random.randint(3, (display_size / 2) - 3)

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10
            if event.key == pygame.K_UP:
                lead_y -= 10
            if event.key == pygame.K_DOWN:
                lead_y += 10
        if event.type == pygame.KEYUP:
            position = math.sqrt((treasure_x - lead_x) ** 2 + (treasure_y - lead_y) ** 2)
            position = round(position,3)
            if position <= 6:
                print('Well done! You have found the treasure!!')
                beep = mixer.Sound('beep2.wav')
                beep.play()
                time.sleep(5)
            else:
                print('You are ' + str(position) + ' metres from the treasure!')

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    pygame.draw.rect(gameDisplay, white, [treasure_x, treasure_y, 4, 4])
    pygame.display.update()

pygame.quit()
quit()





