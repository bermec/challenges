'''
This challenge courtesy of user nagasgura

In this challenge, we read in a string from standard input and output
the translation to or from morse code on standard output.

When translating to Morse code, one space should be used to separate
morse code letters, and two spaces should be used to separate morse
code words. When translating to English, there should only be one
space in between words, and no spaces in between letters.

Here's a chart of the morse code symbols: [1]
http://www.w1wc.com/pdf_files/international_morse_code.pdf

Example input and output: 'sos' -> '... --- ...' '... --- ...' -> 'sos'

'''

char2morse = {
          "!": "---.",      "\"": ".-..-.",     "$": "...-..-",    "'": ".----.",
          "(": "-.--.",      ")": "-.--.-",     "+": ".-.-.",      ",": "--..--",
          "-": "-....-",     ".": ".-.-.-",     "/": "-..-.",
          "0": "-----",      "1": ".----",      "2": "..---",      "3": "...--",
          "4": "....-",      "5": ".....",      "6": "-....",      "7": "--...",
          "8": "---..",      "9": "----.",
          ":": "---...",     ";": "-.-.-.",     "=": "-...-",      "?": "..--..",
          "@": ".--.-.",
          "A": ".-",         "B": "-...",       "C": "-.-.",       "D": "-..",
          "E": ".",          "F": "..-.",       "G": "--.",        "H": "....",
          "I": "..",         "J": ".---",       "K": "-.-",        "L": ".-..",
          "M": "--",         "N": "-.",         "O": "---",        "P": ".--.",
          "Q": "--.-",       "R": ".-.",        "S": "...",        "T": "-",
          "U": "..-",        "V": "...-",       "W": ".--",        "X": "-..-",
          "Y": "-.--",       "Z": "--.."}


message = ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."
print(message)

message = message.split('  ')
msg = ''
for x in message:
    # space between words
    if not msg == '':
        msg += ' '
    x = x.split()
    for y in x:
        for letter, code in char2morse.items():
            if code == y:
                msg += letter.lower()

print(msg)

message = 'python is best!'

message = message.split()
coded_message = ''
for x in message:
    # space between "words"
    if not coded_message == '':
        coded_message += '  '
    for y in x:
        y = y.upper()
        for letter, code in char2morse.items():
            if letter == y:
                coded_message += code + ' '

print('Morse: "python is best"', coded_message)



