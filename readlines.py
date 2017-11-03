
from random import randrange


def sattoloCycle(items):
    ''' str -> str
    shuffle string'''
    apos = ''

    items = list(items)
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    item_string = ''
    for item in items:
        item_string += item

    return item_string


if __name__ == '__main__':
    
    txt = "Ac'cording to a research team at Cambridge University, it doesn't matter in what \
    order the letters in a word are, the only important thing is that the first and \
    last letter be in the right place. The rest can be a total mess and you can still \
    read it without a problem. This is because the human mind does not read every letter \
    by itself, but the word as a whole. Such a condition is appropriately called Typoglycemia."

    txt = txt.split()
    txt = list(txt)
    print(txt)

    output = ''
    out_string = ''

    for word in txt:
        new_word = word
        if len(word) > 3:
            temp = new_word[1:-1]
            if "'" in temp:
                index = temp.find("'")
                to_shuffle = temp.replace("'", '')
            else:
                to_shuffle = temp
            new_word = sattoloCycle(to_shuffle)
            output = word[0] + new_word + word[-1]
            if "'" in word:
                output2 = output[:index + 1] + temp[index] + output[index + 1:]
                out_string = out_string + output2 + ' '
            else:
                #output = word[0] + new_word + word[-1]
                out_string = out_string + output + ' '

        else:
            out_string = out_string + word + ' '
    print(out_string)
