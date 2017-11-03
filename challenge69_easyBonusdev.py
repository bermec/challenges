'''
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


# in the name
def total_width(leng):
    return leng + 3

# upper and lower stripe, first column
def outer(leng):
    return '+' + ('-' * (total_width(leng) + 1)) + '+'

# stripe, mid column
def midColumn(leng):
    return ('-' * (total_width(leng) + 1)) + '+'

# stripe, outer column
def outerColumn(leng):
    return ('-' * (total_width(leng) + 1)) + '+'

# header .....
def headercentre(title, leng, width):
    return '|  '+ title.center(leng) + '  |'

def headerright(title, leng, width):
    return '  ' + title.center(leng) + '  |'

def header(title, leng, width):
    return '|  '+ title.ljust(leng) + '  |'


# content .....
def contentcentre(title, leng, width):
    return '  '+ title.ljust(leng) + '  |'

def contentright(title, leng, width):
    return '  ' + title.ljust(leng) + '  |'

def content(title, leng, width):
    return '|  '+ title.ljust(leng) + '  |'


if __name__ == '__main__':

    #length of longest word in first column
    leng1 = max(len(bonus_titles[0]), len(bonus_wordlist[0][0]),
                        len(bonus_wordlist[1][0]), len(bonus_wordlist[2][0]))
    # second column
    leng2 = max(len(bonus_titles[1]), len(bonus_wordlist[0][1]),
                        len(bonus_wordlist[1][1]), len(bonus_wordlist[2][1]))
    # third column
    leng3 = max(len(bonus_titles[2]), len(bonus_wordlist[0][2]),
                        len(bonus_wordlist[1][2]), len(bonus_wordlist[2][2]))
    width2 = total_width(leng2)
    print(leng2)
    stripe2 = outer(leng1)

    firsttitle = bonus_titles[0]
    secondtitle = bonus_titles[1]
    thirdtitle = bonus_titles[2]

    # name, address, description
    head_a = headercentre(firsttitle, leng1, width2)
    head_b = headerright(secondtitle, leng2, width2)
    head_c = headerright(thirdtitle, leng3, width2)

    content1 = bonus_wordlist[0][0]
    content1a = bonus_wordlist[0][1]
    content1b = bonus_wordlist[0][2]

    content2 = bonus_wordlist[1][0]
    content2a = bonus_wordlist[1][1]
    content2b = bonus_wordlist[1][2]

    content3 = bonus_wordlist[2][0]
    content3a = bonus_wordlist[2][1]
    content3b = bonus_wordlist[2][2]

    content1 = content(content1, leng1, width2)
    content1a = contentcentre(content1a, leng2, width2)
    content1b = contentright(content1b, leng3, width2)

    content2 = content(content2, leng1, width2)
    content2a = contentcentre(content2a, leng2, width2)
    content2b = contentright(content2b, leng3, width2)

    content3 = content(content3, leng1, width2)
    content3a = contentcentre(content3a, leng2, width2)
    content3b = contentright(content3b, leng3, width2)

    midStripe = midColumn(leng2)
    outerStripe = outerColumn(leng3)

    print(stripe2, end= '')
    print(midStripe, end= '')
    print(outerStripe)
    print(head_a, end= '')
    print(head_b, end= '')
    print(head_c)
    print(stripe2, end= '')
    print(midStripe, end= '')
    print(outerStripe)

    print(content1, end= '')
    print(content1a, end= '')
    print(content1b)
    print(stripe2, end= '')
    print(midStripe, end= '')
    print(outerStripe)


    print(content2, end= '')
    print(content2a, end= '')
    print(content2b)
    print(stripe2, end= '')
    print(midStripe, end= '')
    print(outerStripe)

    print(content3, end= '')
    print(content3a, end= '')
    print(content3b)
    print(stripe2, end= '')
    print(midStripe, end= '')
    print(outerStripe)
