
''' A handful of words have their letters in alphabetical order,
that is nowhere in the word do you change direction in the word if
you were to scan along the English alphabet. An example is the word
"almost", which has its letters in alphabetical order.

Your challenge today is to write a program that can determine if the
letters in a word are in alphabetical order.

As a bonus, see if you can find words spelled in reverse alphebatical order.
'''

def alpha_order(lst):
    out_list = []
    for word in lst:
        state = 0
        for x in range(1, len(word)):
            if word[x] >= word[x - 1]:
                if x == len(word) - 1 and state == 0:
                    out_list.append((word, ' IN ORDER'))
                if x == len(word) - 1 and state == 1:
                    out_list.append((word, ' IN REVERSE ORDER'))
                continue
            else:
                state += 1
                if state == 2:
                    out_list.append((word, 'OUT OF ORDER'))
                word = word[::-1]
                continue
    return out_list


if __name__ == '__main__':

    word_list = ['billowy', 'biopsy', 'chinos', 'defaced', 'chintz', 'sponged','bijoux',
     'abhors', 'fiddle', 'begins', 'chimps', 'wronged']
    ans = alpha_order(word_list)
    for x in range(0, len(ans)):
        print(ans[x][0].strip(''),ans[x][1].strip(''))

