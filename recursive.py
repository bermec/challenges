''' Bonus 2: See which numbers don't get palindromic in under 10000 steps.
Numbers that never converge are called Lychrel numbers.
'''
'''
import sys
sys.setrecursionlimit(10000

number = 196
original_number = number
steps = 0

def make_palindrome(number):
    global steps
    if str(number) == ((str(number))[::-1]):
        print( "{0} gets palindromic after {1} steps: {2}".format(original_number, steps, number))
    else:
        steps += 1
        if steps == 996:
            return print("995 recursive steps, max")

        make_palindrome(number + (int(str(number)[::-1])))

make_palindrome(number)
'''

def collect_folders(start):
    stack = [start.id]
    folder_ids = []
    while stack:
        cur_id = stack.pop()
        folder_ids.append(cur_id)
        stack.extend(folder.id for folder in getChildFolders(cur_id))
    return folder_ids