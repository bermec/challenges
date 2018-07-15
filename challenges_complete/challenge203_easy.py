'''
Description

All great things start with something small. Sometimes people don't even realise
what goes into making a 'small' thing.

A popular story is linked above about a group of graphics programmers who create a
rendering engine in some amount of time. After some time HR came to see what the
programmers had accomplished. They responded by showing a black triangle on a tv.

HR was less than impressed (understandle for a non techie) but it goes to show
the natural evolution of a program. What they didn't realise is that the programmers
have created their base engine and can now easily add and extend on top of it.

Maybe you can follow similar steps?
Challenge

On your screen, display a square.

You may use any libraries available to you.

The square may be of any size and of any colour.

'''

import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (128, 128, 128)
colour_list = [black, red, green, grey]

pygame.init()

line_width = 10
width = 800
height = 600


gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Black Square')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(white)

    # draw timeline
    pygame.draw.rect(gameDisplay, black, [400, 400, 4, 4])


    pygame.display.update()
pygame.quit()
quit()

