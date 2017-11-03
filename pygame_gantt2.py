import re
from datetime import datetime as dt


def ordinal(ordinal_dates):
    '''iso8601 to ordinal'''
    dates_ordinal = []
    dates_orig = []
    for x in range(0, len(ordinal_dates)):
        test = ordinal_dates[x]
        d = dt.strptime(ordinal_dates[x], '%Y-%m-%d')
        print("d: " + str(d))
        dates_ordinal.append(d.timestamp())
        dates_orig.append(d)
    print("dates_ordinal: " + str(dates_ordinal))
    period = dates_ordinal[1] - dates_ordinal[0]
    return period, dates_ordinal[0], dates_ordinal[1], dates_orig


def date_to_iso(lst):
    iso = []
    target = re.findall('[^\/]\d+', lst[0])
    iso.append( '20' + target[2] + '-' + target[1] + '-' + target[0])
    return iso


if __name__ == '__main__':
    strng = '''Summary
entry 1
Start Date
08/02/17 00:00
End Date
10/02/17 00:00

Summary
entry 2
Start Date
07/02/17 00:00
End Date
10/02/17 00:00

Summary
entry 3
Start Date
21/02/17 00:00
End Date
25/02/17 00:00'''


    constant_dates = '2017-02-07 2017-02-25'
    # extract dates
    dates = re.findall('\d+\-\d+\-\d+', constant_dates)
    # dates of first project to use as constants
    constant_period = ordinal(dates)[0]
    print('constant: ', constant_period)
    constant_start_date = ordinal(dates)[1]
    constant_end_date = ordinal(dates)[2]
    print('constant_start_date: ', constant_start_date)

    # divide period by 20k to provide a working timeline
    timeline = int(constant_period / 2000)

    epoch_list = []
    project_start_date_list = []

    for line in strng.splitlines():
        line = line.strip()

        dates = re.findall('\d+\/\d+\/\d+', line)
        print("regex dates:" + str(dates))
        if not dates:
            continue
        else:
            dates = date_to_iso(dates)
            epoch_list.append(ordinal(dates))
            project_start_date_list.append(ordinal(dates)[1])
        percent_list = []
        for data in epoch_list:
            percent_start = int(((data[1] - constant_start_date) / constant_period) * 100)
            percent_end = int(((data[2] - constant_start_date) / constant_period) * 100)
            percent_list.append((percent_start, percent_end))
        print('percent_list_end_dates: ', percent_list)

        print(epoch_list)
        print(project_start_date_list)






import pygame

pygame.init()

white = (255, 255, 255)
black =(0, 0, 0)
red =(255, 0, 0)
green = (0, 255, 0)
grey = (128, 128, 128)


gameDisplay = pygame.display.set_mode((700, 300))
pygame.display.set_caption('Gantt')

#pygame.display.update()

gameExit = False

width = timeline
depth = 5
start = 10

while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [start, 100, width, depth])
    pygame.draw.rect(gameDisplay, black, [start + ((57 / 100) * width), 120, start + ((59 / 100) * width) - ((57 / 100) * width), depth + 10])
    pygame.draw.rect(gameDisplay, red, [start + ((10/100) * width), 140, start + ((12/100) * width) - ((10/100) * width), depth + 10])

    pygame.draw.rect(gameDisplay, green, [start + ((18/100) * width), 160, start + ((26/100) * width) - ((18/100) * width), depth +10])

    pygame.draw.rect(gameDisplay, grey,
                     [start + ((10 / 100) * width), 180, start + ((83 / 100) * width) - ((10 / 100) * width),
                      depth + 10])

    pygame.draw.rect(gameDisplay, green,
                     [start + ((10 / 100) * width), 200, start + ((59 / 100) * width) - ((10 / 100) * width),
                      depth + 10])
    pygame.display.update()
pygame.quit()
quit()

