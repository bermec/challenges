''' Imagine each letter and its position within the alphabet.
Now assign each letter its corresponding value ie a=1,
b=2,... z=26. When given a list of words, order the words
by the sum of the values of the letters in their names.

Example: Shoe and Hat

Hat: 8+1+20 = 29

Shoe: 19+8+15+5 = 47

So the order would be Hat, Shoe.

For extra points, divide by the sum by the number of
letters in that word and then rank them.
'''
sentence = 'four suet puds were made warm'
# -- create alphabet list --------------------
ans = []
ans = enumerate(list(map(chr, range(97, 123))))

#-- number the list using a dictionary ----------
dikt = {}
for ind, itm in enumerate(ans, start = 1):
    dikt[itm[1]] = itm[0]

acc = 0
dikt2 = {}
#-- split the sentence into words ------
sentence = sentence.split()

# -- sum the values -----------
for word in sentence:
    for char in word:
        char = dikt.get(char)
        acc += char
    dikt2[word] = acc
    acc = 0

# -- order them by value -------------
from collections import Counter
#To sort in reverse order
sorted_dikt2 = Counter(dikt2).most_common()
for y in range(0, len(sorted_dikt2)):
    print(sorted_dikt2[y][0],' ', end='')