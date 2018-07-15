'''

Bonus 1: One word in the list has 33 other words that can appear next to it. What is this word?

Bonus 2: How many different words can be reached, starting from best, in 3 or fewer steps?
'''
import re


def list_count(lst, word):
    if len(lst) == 33:
        return word
    else:
        return False


if __name__ == '__main__':
    word_set = set()
    with open('selected_four_letter_words.txt') as f:
        for line in f:
            line = line.strip()
            word_set.add(line)

    output = list()
    alpha_string = 'abcdefghijklmnopqrstuvwxyz'

    #word_set2 = ['best', 'puma']
    for word in word_set:
        output = []
        for letter in word:
            for item in alpha_string:
                sub_word = re.sub(letter, item, word)
                if sub_word in word_set:
                    if sub_word == word:
                        continue
                    if sub_word not in output:
                        output.append(sub_word)

        result = list_count(output, word)
        if result == False:
            continue
        else:
            print(result)
            exit()

