''' write a program that takes

input : a file as an argument

output: counts the total number of lines.

for bonus, also count the number of words in the file.

'''

with open('mbox-short.txt', 'r') as f:
    acc = 0
    word_count = 0
    for line in f:
        acc += 1
        line = line.split()
        for word in line:
            word_count += 1

print(acc, word_count)