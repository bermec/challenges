import re

text_string = ''
word_dict = {}
with open('gutenburg.txt') as f:
    for line in f:
        line = line.rstrip()
        text_string += line + ' '
    #txt = text_string.split()
    #print(txt)
    txt = re.findall('Title:.*Patagonia.', text_string)
    txt = txt[0]
    #print(txt)
    txt = re.findall('[a-zA-Z]+', txt)
    for word in txt:
        word_dict[word] = word_dict.setdefault(word, 0) + 1

print(word_dict)