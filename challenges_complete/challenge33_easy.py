''' This would be a good study tool too. I made one myself and I thought it would also be a good challenge.

Write a program that prints a string from a list at random, expects input, checks for a right or wrong answer,
and keeps doing it until the user types "exit". If given the right answer for the string printed,
it will print another and continue on. If the answer is wrong, the correct answer is printed and
the program continues.

Bonus: Instead of defining the values in the program, the questions/answers is in a file,
formatted for easy parsing.

Example file:s
Translate: hola,hello
'''


dikt = {'4 times 8 =  ': 32, '6 divided by 3 =  ': 2, 'Square root of nine?  ': 3}

for key in dikt:
    question = key
    ans = input(question)
    ans1 = str(dikt[question])
    if ans == ans1:
        print('Correct')
    else:
        print('Wrong! Answer is:  ', dikt[question])
