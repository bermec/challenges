'''
Help! My keyboard is broken, only a few keys work any more.
If I tell you what keys work, can you tell me what words I can write?

(You should use the trusty enable1.txt file, or /usr/share/dict/words
to chose your valid English words from.)
Input Description

You'll be given a line with a single integer on it,
telling you how many lines to read. Then you'll be given that many lines,
each line a list of letters representing the keys that work on my keyboard. Example:

3
abcd
qwer
hjklo

Output Description

Your program should emit the longest valid English language
word you can make for each keyboard configuration.

abcd = bacaba
qwer = ewerer
hjklo = kolokolo

Challenge Input

4
edcf
bnik
poil
vybu

Challenge Output

edcf = deedeed
bnik = bikini
poil = pililloo
vybu = bubby

'''


def long_word(kbd):
    output = []
    for keyboard in kbd:
        temp = ''
        lst = []
        with open('enable1.txt') as f:
            for word in f:
                word = word.strip('\n')
                for letter in word:
                    if letter in keyboard:
                        temp += letter
                        if len(word) == len(temp):
                            lst.append(temp)
                            temp = ''
                        continue
                    else:
                        temp = ''
                        break

        long = sorted(lst, key= len)

        output.append(long[-1])
    return output

def main():
    kboard = 'abcd,qwer,hjklo'
    kboard = kboard.split(',')


    kboard2 = '''edcf,bnik,poil,vybu'''
    kboard2 = kboard2.split(',')


    ans = long_word(kboard)
    for x in range(0, len(ans)):
        print('{0}{1}{2}'.format(kboard[x], ' = ',ans[x]))
    print()

    ans2 = long_word(kboard2)
    for x in range(0, len(ans2)):
        print('{0}{1}{2}'.format(kboard2[x], ' = ',ans2[x]))

if __name__ == '__main__':
    main()

