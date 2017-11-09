'''
Unix, the famous multitasking and multi-user operating system, has several standards that defines Unix
commands, system calls, subroutines, files, etc. Specifically within Version 7 (though this is included
in many other Unix standards), there is a game called "arithmetic". To quote the Man Page:

Arithmetic types out simple arithmetic problems, and waits for an answer to be typed in. If the answer
is correct, it types back "Right!", and a new problem. If the answer is wrong, it replies "What?", and
waits for another answer. Every twenty problems, it publishes statistics on correctness and the time
required to answer.

Your goal is to implement this game, with some slight changes, to make this an [Easy]-level challenge.
You will only have to use three arithmetic operators (addition, subtraction, multiplication) with four
integers. An example equation you are to generate is "2 x 4 + 2 - 5".

Author: nint22
Formal Inputs & Outputs
Input Description

The first line of input will always be two integers representing an inclusive range of integers you are to
pick from when filling out the constants of your equation. After that, you are to print off a single
equation and wait for the user to respond. The user may either try to solve the equation by writing the
nteger result into the console, or the user may type the letters 'q' or 'Q' to quit the application.
Output Description

If the user's answer is correct, print "Correct!" and randomly generate another equation to show to the user.
Otherwise print "Try Again" and ask the same equation again. Note that all equations must randomly pick and
place the operators, as well as randomly pick the equation's constants (integers) from the given range.
You are allowed to repeat constants and operators. You may use either the star '*' or the letter 'x'
characters to represent multiplication.
Sample Inputs & Outputs
Sample Input / Output

Since this is an interactive application, lines that start with '>' are there to signify a statement from
the console to the user, while any other lines are from the user to the console.

0 10
> 3 * 2 + 5 * 2
16
> Correct!
> 0 - 10 + 9 + 2
2
> Incorrect...
> 0 - 10 + 9 + 2
3
> Incorrect...
> 0 - 10 + 9 + 2
1
> Correct!
> 2 * 0 * 4 * 2
0
> Correct!

# Multiplier first to simplify the maths (order of operations)
'''
import random

def maths(a, b):
    operators = ['-', '+',]
    mult = ['*']
    equation = ''
    accum = 0
    num_list = []
    while accum < 4:
        num = random.randint(a, b)
        num_list.append(num)
        accum += 1

    reserve = random.choice([0, 1])
    num = random.randint(0, 4)

    flag = True
    for x in range(0, len(num_list)-1):
        equation += str(num_list[x])
        try:
            equation += mult[x]
        except IndexError:
            flag = False

        if flag == False:
            try:
                equation += operators[x]
            except IndexError:
                equation += str(operators[reserve])
    equation += str(num_list[-1])

    # clean space to use eval
    newspace = {'__builtins__': None}
    ans = eval(equation, newspace)
    return (equation, ans)


if __name__ == '__main__':
    low = 0
    high = 10
    equation_plus_answer = maths(low, high)
    expression = equation_plus_answer[0]
    ans = equation_plus_answer[1]
    print('Type answer or "q" to quit: ')
    guess = None
    while guess != 'q':
        equation_plus_answer = maths(low, high)
        expression = equation_plus_answer[0]
        ans = equation_plus_answer[1]
        print('Answer please...')
        guess = input('> ' + expression)
        if guess == 'q':
            exit()
        elif int(guess) == ans:
            print('Correct!')
        elif guess == 'q':
            exit()
        else:
            while True:
                if guess == 'q':
                    exit()
                elif int(guess) != ans:
                    print(ans)
                    print('Incorrect... ' + '\n' + 'Try Again ')
                    guess = input('> ' + expression)
                    #guess = ans
                else:
                    break


        if guess == 'q':
            exit()
