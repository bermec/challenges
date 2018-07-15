''' Write a program that will accept a sentence as input and then output that sentence surrounded by some type of an ASCII decoratoin banner.

Sample run:

Enter a sentence: So long and thanks for all the fish

Output

*****************************************
*                                       *
*  So long and thanks for all the fish  *
*                                       *
*****************************************

Bonus: If the sentence is too long, move words to the next line.

'''


def outer():
    global leng
    return ('x' * (leng +6))

def inner():
    global leng
    return ('x' + (' ' * (leng + 4)) + 'x')

def string():
    global quote
    return ('x' + ' ' * 2 + quote + ' ' * 2 + 'x')


if __name__ == '__main__':

    quote = input("Let's have a quote...:  ")
    leng = len(quote)

    out = outer()
    inn = inner()
    txt = string()

    print(out + "\n" + inn + "\n" + txt + "\n" + inn + "\n" + out)