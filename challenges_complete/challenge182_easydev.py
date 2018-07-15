'''
 (Easy): The Column Conundrum

Text formatting is big business. Every day we read information in one of several formats.
Scientific publications often have their text split into two columns, like this.
Websites are often bearing one major column and a sidebar column, such as Reddit itself.
Newspapers very often have three to five columns. You've been commisioned by some bloke
you met in Asda to write a program which, given some input text and some numbers, will
split the data into the appropriate number of columns.
Formal Inputs and Outputs
Input Description

To start, you will be given 3 numbers on one line:

<number of columns> <column width> <space width>

    number of columns: The number of columns to collect the text into.
    column width: The width, in characters, of each column.
    space width: The width, in spaces, of the space between each column.

After that first line, the rest of the input will be the text to format.
Output Description

You will print the text formatted into the appropriate style.

You do not need to account for words and spaces. If you wish, cut a word into two,
so as to keep the column width constant.
Sample Inputs and Outputs
Sample Input

Input file is available here. (NB: I promise this input actually works this time, haha.)
Sample Output

Outout, according to my solution, is available here. I completed the Extension challenge too -
you do not have to account for longer words if you don't want to, or don't know how.
'''




if __name__ == "__main__":
    import re
    format_style = [4, 25, 1]

    with open('holmes.txt', 'r') as f:
        f = f.read()
        sample = re.findall('.{25}', f)
        #print(sample)


    for x in range(0, 125, 4):
        temp = sample[x]
        if x > 0 and x%3 == 0:
            print('{0}{1:<25}'.format('9  ',sample[x]))
        else:
            print('{0}{1:<25}'.format('9  ', sample[x]), end='')


    #print('{0:<10}{1:<10}{3}{2:<10}'.format('red', 'balloonssy', 'large', ' '))
    #print('{0:<10}{1:<10}{2:<10}'.format('reddish', 'balloon', 'largely'))