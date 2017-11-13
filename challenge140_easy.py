'''When writing code, it can be helpful to have a standard (Identifier naming convention)
that describes how to define all your variables and object names. This is to keep code
easy to read and maintain. Sometimes the standard can help describe the type (such as in
Hungarian notation) or make the variables visually easy to read (CamcelCase notation or
snake_case).

Your goal is to implement a program that takes an english-language series of words and
converts them to a specific variable notation format. Your code must support CamelCase,
snake_case, and capitalized snake_case.
Formal Inputs & Outputs
Input Description

On standard console input, you will be given an integer one the first line of input,
which describes the notation you want to convert to. If this integer is zero ('0'), then
use CamelCase. If it is one ('1'), use snake_case. If it is two ('2'), use capitalized
snake_case. The line after this will be a space-delimited series of words, which will
only be lower-case alpha-numeric characters (letters and digits).
Output Description

Simply print the given string in the appropriate notation.
Sample Inputs & Outputs
Sample Input

0
hello world

1
user id

2
map controller delegate manager

Sample Output

0
helloWorld

1
user_id

2
MAP_CONTROLLER_DELEGATE_MANAGER

Difficulty++

For an extra challenge, try to convert from one notation to another.
Expect the first line to be two integers, the first one being the
notation already used, and the second integer being the one you are
to convert to. An example of this is:

Input:

1 0
user_id

Output:

userId
'''
import re


def Camel_Case(l):
    output = ''
    for x in range(0, len(l)):
        if x == 0:
            temp = l[x]
            temp = temp.lower()
        else:
            temp = l[x]
            temp = temp.title()
        output += temp
    return output


def snake_case(l):
    output = ''
    for x in range(0, len(l)):
        temp = l[x]
        temp = temp.lower()
        if temp == l[-1]:
            output += temp
        else:
            output += temp + '_'
    return output


def Capitalized_snake_case(l):
    output = ''
    for x in range(0, len(l)):
        temp = l[x]
        temp = temp.lower()

        if temp == l[0]:
            temp = temp.title()
            output += temp + '_'
        elif temp == l[-1]:
            output += temp
        else:
            output += temp + '_'
    return output

if __name__ == '__main__':
    candidates = '''0
    hello world
    
    1
    user id
    
    2
    map controller delegate manager
    '''

    num_list = []
    word_list = []
    candidates = candidates.splitlines()

    for line in candidates:
        num = re.findall('[0-9]', line)
        words = re.findall('([a-zA-Z]+)', line)
        if len(num) > 0:
            try:
                num_list.append(num[0])
            except IndexError:
                pass
        if len(words) > 0:
            try:
                word_list.append(words)
            except IndexError:
                pass

    for x in range (0, len (num_list)):
        if num_list[x] == '0':
            ans1 = Camel_Case(word_list[x])
        elif num_list[x] == '1':
            ans2 = snake_case(word_list[x])
        else:
            ans3 = Capitalized_snake_case(word_list[x])


    print('{0}{3}{1}{3}{2}'.format(ans1, ans2, ans3, '\n'))