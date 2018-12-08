'''
Compression makes use of the fact that repeated structures are redundant,
and it's more efficient to represent the pattern and the count or a
reference to it. Siimilarly, we can condense a sentence by using the
redundancy of overlapping letters from the end of one word and the start
of the next. In this manner we can reduce the size of the sentence, even
if we start to lose meaning.

For instance, the phrase "live verses" can be condensed to "liverses".

In this challenge you'll be asked to write a tool to condense sentences.
Input Description

You'll be given a sentence, one per line, to condense. Condense where you
can, but know that you can't condense everywhere. Example:

I heard the pastor sing live verses easily.

Output Description

Your program should emit a sentence with the appropriate parts condensed
away. Our example:

I heard the pastor sing liverses easily.

Challenge Input

Deep episodes of Deep Space Nine came on the television only after the news.
Digital alarm clocks scare area children.

Challenge Output

Deepisodes of Deep Space Nine came on the televisionly after the news.
Digitalarm clockscarea children.

'''

def shortest(a, b):
    if len(a) <= len(b):
        len_word = len(a)
    else:
        len_word = len(b)
    return len_word + 1


candidates = 'Digital alarm clocks scare area children.'
compressed_word = ''
output = ''
candidates = candidates.split()
pair = False
co_joined = False

for x in range(0, len(candidates) - 1):
    candidate1 = candidates[x]
    candidate2 = candidates[x + 1]
    # if there is a compressed word previously
    if co_joined:
        candidate1 = compressed_word
        co_joined = False
    length_word = shortest(candidate1, candidate2)
    for y in range(1, length_word):
        rear_slice = candidate1[y * -1:]
        front_slice = candidate2[:y]

        # check if pattern matches and word is a single letter.
        if rear_slice == front_slice and rear_slice == candidate1[0]:
            co_joined = True
            if co_joined:
                compressed_word = candidate2
            continue

        # if rear slice == front slice keep going till they don't.
        elif rear_slice == front_slice:
            temp = [rear_slice, front_slice]
            words = [candidate1, candidate2]
            index = y
            pair = True
            continue
        else:
            # now does not match so join up new word (*previous was a pair).
            if not rear_slice == front_slice and pair:
                words = [candidate1, candidate2]
                word = words[0] + words[1][y - 1:]
                compressed_word = word
                co_joined = True
                pair = False
                word = ''
                words = []
                break

            elif not rear_slice == front_slice and y == length_word - 1:
                output += candidate1 + ' '
                break
            else:
                pass

output += candidate2
print(output)