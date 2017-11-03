''' Write a program that takes a title and a list as input
and outputs the list in a nice column. Try to make it so
the title is centered. For example:

title: 'Necessities'
input: ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls']

output:

    +---------------+
    |  Necessities  |
    +---------------+
    | fairy         |
    | cakes         |
    | happy         |
    | fish          |
    | disgustipated |
    | melon-balls   |
    +---------------+

Bonus: amend the program so that it can output a two-dimensional
table instead of a list. For example, a list of websites:

titles: ['Name', 'Address', 'Description']
input:  [['Reddit', 'www.reddit.com', 'the frontpage of the internet'],
        ['Wikipedia', 'en.wikipedia.net', 'The Free Encyclopedia'],
        ['xkcd', 'xkcd.com', 'Sudo make me a sandwich.']]

output:

    +-----------+------------------+-------------------------------+
    |   Name    |     Address      |          Description          |
    +-----------+------------------+-------------------------------+
    | Reddit    | www.reddit.com   | the frontpage of the internet |
    +-----------+------------------+-------------------------------+
    | Wikipedia | en.wikipedia.net | The Free Encyclopedia         |
    +-----------+------------------+-------------------------------+
    | xkcd      | xkcd.com         | Sudo make me a sandwich       |
    +-----------+------------------+-------------------------------+

'''



title = 'Necessities'
wordlist = ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls']

bonus_titles = ['Name', 'Address', 'Description']
bonus_wordlist = [['Reddit', 'www.reddit.com', 'the frontpage of the internet'],
        ['Wikipedia', 'en.wikipedia.net', 'The Free Encyclopedia'],
        ['xkcd', 'xkcd.com', 'Sudo make me a sandwich.']]

# find length of longest word in list
def length_of_word(lst):
    leng = 0
    for word in wordlist:
        temp_leng = len(word)
        if temp_leng  >= leng:
            leng = temp_leng
    return leng



def total_width(leng):
    return leng + 3

def outer(leng):
    return '+' + ('-' * (total_width(leng) + 1)) + '+'

def outerColumns(leng):
    return ('-' * (total_width(leng) + 1)) + '+'


def headerfirst(title, leng, width):
    return '|  '+ title.center(leng) + '  |'

def headerright(title, leng, width):
    return '|  '+ title.center(leng) + '  |'

def header(title, leng, width):
    return '|  '+ title.ljust(leng) + '  |'

def content(wordlist):
    global leng
    content_string = ''
    for word in wordlist[:-1]:
        content_string += '|  ' + word.ljust(leng) + '  |\n'
    else:
        content_string += '|  ' + wordlist[-1].ljust(leng) + '  |'

    return  content_string


if __name__ == '__main__':
    leng = max(length_of_word(wordlist), len(title))
    print('leng', leng)
    width = total_width(leng)
    head1 = header(title, leng, width)
    stripe = outer(leng)
    ans2 = content(wordlist)
    print(stripe)
    print(head1)
    print(stripe)
    print(ans2)
    print(stripe)

