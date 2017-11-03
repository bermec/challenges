'''
This challenge comes to us from nagasgura

The human body goes through 90 minute sleep cycles during the night,
and you feel more refreshed if you wake up at the end of a sleep
cycle than if you wake up during a sleep cycle. The challenge is to
make a program that takes a wake-up time and outputs the possible
times to fall asleep so that you will wake up at the end of a sleep
cycle.

Example:

Input (Wake-up time): 6:15 AM

Output (when to go to sleep): 9:15 PM, 10:45 PM, 12:15 AM, or 1:45 AM

Bonus 1: Be able to input a sleep time and output potential wake-up times

Bonus 2: Account for how long it takes to fall asleep

'''
import datetime
import re

t = input('Enter wake-up time in 00:00 format:  ')
print('15 minute "fall asleep time allowed"')
print()
#t = '6:15'
format_t = '%H:%M'
doze = 15
t1 = datetime.datetime.strptime(t, format_t)
t2 = datetime.timedelta(minutes=90)
doze_time = datetime.timedelta(minutes=doze)

for x in range(6, 2, -1):
    t4 = (t1 - (t2 * x) - doze_time)
    kip = str(x) + ' hrs  ' + str(t4)

    first_time = re.findall('\S\s(\d+\:\d+)', kip)
    output = datetime.datetime.strftime(t4, '%I:%M %p')
    print('To bed: ', output)
print()
print('Wake at', datetime.datetime.strftime(t1, '%I:%M %p'))
