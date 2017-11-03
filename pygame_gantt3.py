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

def timelines(lst):
    result = []
    lst = sorted(lst)
    result.append(lst[0])
    result.append(lst[-1])
    line = ordinal(result)[0]
    return line




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
    timeline_data_list = []
    epoch_list = []
    project_start_date_list = []
    date_pairs = []
    # read in data
    for line in strng.splitlines():
        line = line.strip()

        dates = re.findall('\d+\/\d+\/\d+', line)
        # if dates contain data
        if dates:
            dates = date_to_iso(dates)
            timeline_data_list.append(dates[0])
            date_pairs.append(dates[0])
        print("regex dates:" + str(dates))
        if not len(date_pairs) == 2:
            continue
        else:
            data = ordinal(date_pairs)
            epoch_list.append(data)
            start_date = data[1]
            project_start_date_list.append(start_date)
            date_pairs = []

    timeline = int(timelines(timeline_data_list) / 2000)


    percent_list = []
    for data in epoch_list:
        percent_start = int(((data[1] - constant_start_date) / constant_period) * 100)
        percent_end = int(((data[2] - constant_start_date) / constant_period) * 100)
        percent_list.append((percent_start, percent_end))
    print('percent_list_end_dates: ', percent_list)

    print('epoch_list: ', epoch_list)
    print(project_start_date_list)


import pygame

pygame.init()

white = (255, 255, 255)
black =(0, 0, 0)
red =(255, 0, 0)
green = (0, 255, 0)
grey = (128, 128, 128)

display_width = 777
display_height = 300
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Gantt')

#pygame.display.update()

gameExit = False
start = 50
width = timeline
depth = 30

font = pygame.font.SysFont(None, 20)

def message_to_screen(msg, color, co_ords):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, co_ords)


while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(white)

    # draw timeline
    pygame.draw.rect(gameDisplay, black, [0, 50, width, 4])

    # draw the three projects
    x = (percent_list[0][0] / 100) * width
    rect_width = ((percent_list[0][1] / 100) * width) - x
    pygame.draw.rect(gameDisplay, black, [x, 80, rect_width, depth], 4)

    x = (percent_list[1][0] / 100) * width
    rect_width = ((percent_list[1][1] / 100) * width) - x
    pygame.draw.rect(gameDisplay, red, [x, 120, rect_width, depth], 4)

    x = (percent_list[2][0] / 100) * width
    rect_width = ((percent_list[2][1] / 100) * width) - x
    pygame.draw.rect(gameDisplay, green, [x, 160, rect_width, depth], 4)

    # project dates
    start_date = 7
    days = 18

    message_to_screen('07/02/17', red, [((7 - start_date) / days) * width, 60])
    message_to_screen('10/02/17', red, [((10 - start_date) / days) * width, 60])
    message_to_screen('14/02/17', red, [((14 - start_date) / days) * width, 60])
    message_to_screen('21/02/17', red, [((21 - start_date) / days) * width, 60])

    day_length = width / 18
    for x in range(1, days):
        pygame.draw.line(gameDisplay, black, (day_length * x, 40), (day_length * x, 50))

    pygame.display.update()
pygame.quit()
quit()

