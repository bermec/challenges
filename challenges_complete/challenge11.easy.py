''' The program should take three arguments. The first will be a day, the second will be month,
and the third will be year. Then, your program should compute the day of the week that date will fall on.
'''
import calendar

date = input('Input day, month, year in the form ../ ../... ')
date = date.split('/')

d = calendar.weekday(int(date[2]), int(date[1]), int(date[0]))
weekday = {0: 'Monday', 1: 'Tuesday', 2:'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

print(weekday[d])