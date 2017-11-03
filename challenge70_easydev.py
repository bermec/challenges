''' Write a program that takes a filename and a parameter n
and prints the n most common words in the file,
and the count of their occurrences, in descending order.
'''
# read the input file
def readfile(file):
    dict = {}
    with open('vshort.txt', 'r') as f:
        lst = []
        for line in f:
            words = line.split()
            for word in words:
                lst.append(word)
    return lst

# count the maximum occurance of a word and place
# results a a dictionary
def count(lst):
    global dikt
    acc = 0
    global wordz
    nn = 0
    for x in range(0, len(lst)):
        temp = lst.count(lst[x])
        if temp > acc:
            acc = temp
            wordz = lst[x]
    dikt[acc] = wordz
    return (lst)

# revove words that have been counted.
def removal(lst):
    global dikt
    global wordz
    for word in lst:
        if word == wordz:
            lst.remove(word)
    return lst



if __name__ == '__main__':
    from collections import OrderedDict
    dikt = {}
    wordz = ''
    file = 'vshort.txt'
    n = 3
    nn = 1
    ans = readfile(file)
    # count and remove till n amounts completed
    while nn <= n:
        nn += 1
        ans1 = count(ans)
        remove = removal(ans1)

    d = OrderedDict(dikt)
    d = OrderedDict(reversed(list(d.items())))
    print(d)