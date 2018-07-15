'''
Description:

You and a friend are working on a very important, bleeding-edge, research paper:
"Computational Complexity of Sorting Pictures of Cats with Funny Text on the Web".
The catch though is your friend wrote his part of the paper with his hands
shifted to the right, meaning the top row of keys he used weren't "QWERTYUIOP"
(regular US keyboard), but instead "WERTYUIOP{".

Your goal is to take what your friend wrote, and convert it from his broken
shifted text back into regular english!

Formal Inputs & Outputs:

Input Description:

String ShiftedText - The shifted text in question. The only chracters you have to
deal with are letters, in both cases, and the following symbols: '{', '[', ':',
';', '<', ','. The space character may be present, but you do not have to shift that.

Output Description:

Print the correct text.

Sample Inputs & Outputs:

The string "Jr;;p ept;f" should shift back, through your function, into "Hello World".
Another example is: "Lmiyj od ,u jrtp", which corrects to "Knuth is my hero"
'''

key_dict_upper = {
    'w': 'q',
    'e': 'w',
    'r': 'e',
    't': 'r',
    'y': 't',
    'u': 'y',
    'i': 'u',
    'o': 'i',
    'p': 'o',
    '[': 'p'}
key_dict_middle = {
    's': 'a',
    'd': 's',
    'f': 'd',
    'g': 'f',
    'h': 'g',
    'j': 'h',
    'k': 'j',
    'l': 'k',
    ';': 'l'}
key_dict_lower = {
    'x': 'z',
    'c': 'x',
    'v': 'c',
    'b': 'v',
    'n': 'b',
    'm': 'n',
    ',': 'm'}
all_dicts = {}
all_dicts = {**key_dict_upper, **key_dict_middle, **key_dict_lower}
incoming_message = 'Jr;;p ept;f'
decoded = ''

for item in incoming_message:
    if item == ' ':
        decoded += ' '
        continue
    # convert to lower
    item_lower = item.lower()
    # check ifin dictionary
    for key, value in all_dicts.items():
        if item_lower == key:
            item_lower = value
            # if it was upper case convert
            if item.isupper():
                decoded += item_lower.upper()
            else:
                decoded += item_lower
            break
print(decoded)
