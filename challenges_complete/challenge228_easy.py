
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
        for x in range(1, len(word)):
            if word[x] >= word[x - 1]:
                if x == len(word) - 1:
                   out_list.append((word, ' IN ORDER'))
                continue
            else:
                word = word[::-1]
                for x in range(1, len(word)):
                    if word[x] >= word[x - 1]:
                        if x == len(word) - 1:
                            out_list.append((word, ' IN ORDER'))
                            break
                    else:
                        out_list.append((word, ' OUT OF ORDER'))
                        continue

    return out_list

def reverse_alpha_order(lst):
    out_list = []
    for word in lst:
        word = word[::-1]
        for x in range(1, len(word)):
            if word[x] >= word[x - 1]:
                if x == len(word) - 1:
                   out_list.append((word, ' IN ORDER'))
                continue
            else:
                out_of_order()
                break
    return out_list

def out_of_order():
    return out_list.append((word, ' NOT IN ORDER'))


if __name__ == '__main__':
    word_lst = ['billowy', 'biopsy', 'chinos', 'defaced', 'chintz', 'sponged','bijoux',
                'abhors', 'fiddle', 'begins', 'chimps', 'wronged']

    ans = alpha_order(word_lst)
    print(ans)

