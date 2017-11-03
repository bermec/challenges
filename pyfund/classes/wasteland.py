import sys

f = open('wasteland.txt', mode= 'wt', encoding='utf-8')
f.write('What are the roots that clutch, ')
f.write('what branches grow\n')
f.write('Out of this stony rubbish? ')
f.close()

''' append to a file'''
h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['Son of man,\n'
     'You cannot say, or guess '
     'for you know only,\n'
     'A heap of broken images, ',
     'where the sun beats\n'])
h.close()






if __name__ == '__main__':
    pass