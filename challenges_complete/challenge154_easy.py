''' It is that time of year again when across some of the lands you hear about March Madness
and NCAA Basketball. People ask about your brackets and how you are doing in your predictions.
Of course to those of us who perform the art of coding we always get a bit confused by this.

You see we think of brackets like [] or {} or () to use in our many wonderful languages.
As it turns out in a bit of madness some messages got the rough bracket treatment.
I am asking you to decode these messages by removing the brackets and decoding the message.
The order of the message should be ordered for the deepest bracket strings to be
displayed first then the next deepest and so forth.
Input:

(String of words with matching bracket sets in an order that can only be called mad)
Example 1:

((your[drink {remember to}]) ovaltine)
Example 2:

[racket for {brackets (matching) is a} computers]
Example 3:

[can {and it(it (mix) up ) } look silly]
Output:

The words separated by a single space in order from deepest
to shallow on the ordering of matched brackets.
Example 1:

remember to drink your ovaltine
Example 2:

matching brackets is a racket for computers
Example 3:

mix it up and it can look silly
'''

import re
import itertools
output = 'remember to drink your ovaltine'
inString = '((your[drink {remember to))) ovaltine)'

# extract the text
extractText = re.findall('\w+', inString)

# generate permutations of the resulting list
lst = list(map(" ".join, itertools.permutations(extractText)))

# find index of required string
theIndex = lst.index(output)
print(lst[theIndex])
