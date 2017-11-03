''' Write a program that can translate Morse code in the format of ...---...

A space and a slash will be placed between words. ..- / --.-

For bonus, add the capability of going from a string to Morse code.

Super-bonus if your program can flash or beep the Morse.

This is your Morse to translate:

.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. /
 --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . /
  -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--

'''

temp = []

dikt = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i',
        '.---': 'j', '-.-': 'k','.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't','..-': 'u', '---.': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '/': ' '}

message = '.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ' \
          '..- -.-. -.- / --- -. / - .... . /  -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--'

message = message.split()

for char in message:
    conv = (dikt[char])
    temp.append(conv)


for item in temp:
    print(item, end=' ')
