'''
Your program will be responsible for analyzing a small chunk of text,
the text of this entire dailyprogrammer description. Your task is to
output the distinct words in this description, from highest to lowest
count with the number of occurrences for each. Punctuation will be
considered as separate words where they are not a part of the word.

The following will be considered their own words: " . , : ; ! ? ( ) [ ] { }

For anything else, consider it as part of a word.

Extra Credit:

Process the text of the ebook Metamorphosis, by Franz Kafka and determine
the top 10 most frequently used words and their counts. (This will help for part 2)

'''

sample = '''Your program will be responsible for analyzing a small chunk of text,
the text of this entire dailyprogrammer description. Your task is to
output the distinct words in this description, from highest to lowest
count with the number of occurrences for each. Punctuation will be
considered as separate words where they are not a part of the word.

The following will be considered their own words: " . , : ; ! ? ( ) [ ] { }

For anything else, consider it as part of a word.

Extra Credit:

Process the text of the ebook Metamorphosis, by Franz Kafka and determine
the top 10 most frequently used words and their counts. (This will help for part 2)
'''
import collections

counter_dict = {}
for line in sample.splitlines():
    line = line.split()
    for word in line:
        counter_dict[word] = counter_dict.get(word, 0) + 1
d = counter_dict

sorted_dict = collections.namedtuple('Word', 'score name')
highest = sorted([sorted_dict(v, k) for (k, v) in d.items()], reverse=True)

print(highest)
