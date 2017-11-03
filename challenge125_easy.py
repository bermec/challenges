'''
You're a newly hired engineer for a brand-new company that's building a
"killer Word-like application". You've been specifically assigned to implement
a tool that gives the user some details on common word usage, letter usage, and
some other analytics for a given document! More specifically, you must read a
given text file (no special formatting, just a plain ASCII text file) and print
off the following details:

    Number of words
    Number of letters
    Number of symbols (any non-letter and non-digit character, excluding white spaces)
    Top three most common words (you may count "small words", such as "it" or "the")
    Top three most common letters
    Most common first word of a paragraph (paragraph being defined as a block of text
with an empty line above it) (Optional bonus)
    Number of words only used once (Optional bonus)
    All letters not used in the document (Optional bonus)


Sample Output

Note that we do not print the "most common first word in paragraphs" in this example,
nor do we print the last two bonus features:

265 words
1812 letters
59 symbols
Top three most common words: "Eu", "In", "Dolor"
Top three most common letters: 'I', 'E', 'S'

'''

import re
word_dict = {}
word_count = []
letter_dict = {}
lead_word = {}
letter_count = 0
symbol_count = 0
num_single_words = []

# number of words
with open('paragraph.txt') as f:
    for line in f:
        line = line.split()
        for word in line:
            word = re.findall('\w+\S?\w|[a-zA-Z]', word)
            if word == []:
                word = ''
            else:
                word = word[0]
            word_count.append(word)
            word_dict[word] = word_dict.get(word, 0) + 1

    word_num = len(word_count)

    # letter and symbol count
    f.seek(0)
    for line in f:
        for letter in line:
            if letter.isalnum():
                letter_dict[letter] = letter_dict.get(letter, 0) + 1
                letter_count += 1
            else:
                if letter != ' ':
                    symbol_count += 1

    # lead words
    f.seek(0)
    output = ''
    flag = True
    for line in f:
        line = line.strip()
        if line == '':
            flag = True
            continue
        elif flag:
            first_word = re.findall('^\w+', line)
            lead_word[first_word[0]] = lead_word.get(first_word[0], 0) + 1
            flag = False

    # number of single words
    for k, v in word_dict.items():
        if v == 1:
            num_single_words.append(k)

# number of single words
number_single_words = len(num_single_words)
# 3 most common letters
sorted_values = sorted(letter_dict, key=letter_dict.get, reverse=True)
# 3 most common words
sorted_words = sorted(word_dict, key=word_dict.get, reverse=True)
# most common first word
lead_word = sorted(word_dict, key=word_dict.get, reverse=True)

# unused letters
unused_letters = []
import string
word_string = string.ascii_lowercase
for letter in word_string:
    if letter in letter_dict:
        continue
    else:
        unused_letters.append(letter)

print('Number of words: ', word_num)
print('Number of letters: ', letter_count)
print('Number of symbols: ', symbol_count)
print('Three most common words: ', sorted_words[:3])
print('Three most common letters: ', sorted_values[:3])
print('Most common first word: ', lead_word[0])
print('Number of words only used once: ', number_single_words)
print('All letters not used in the document: ', unused_letters)





'''

    Number of words
    Number of letters
    Number of symbols (any non-letter and non-digit character, excluding white spaces)
    Top three most common words (you may count "small words", such as "it" or "the")
    Top three most common letters
    Most common first word of a paragraph (paragraph being defined as a block of text with an empty line above it) (Optional bonus)
    Number of words only used once (Optional bonus)
    All letters not used in the document (Optional bonus)
'''