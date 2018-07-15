''' Write a program that accepts a year as input and outputs the century the year belongs in
(e.g. 18th century's year ranges are 1701 to 1800) and whether or not the year is a leap year.
Pseudocode for leap year can be found here.

Sample run:

Enter Year: 1996

Century: 20

Leap Year: Yes

Enter Year: 1900

Century: 19

Leap Year: No
'''


year = input('Enter year:  ')

def leapYear(n):
    if ((n % 4== 0) and  (n % 100 != 0)) or (n % 400 == 0):
        return 'yes'
    else:
        return 'no'

def cent(century):
    century = int(year[ :-2]) + 1
    return  century

if __name__ == '__main__':
    print('Leap Year:  {0}'.format(leapYear(int(year))))
    print('Century:  {0}'.format(cent(int(year))))

