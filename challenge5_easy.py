''' Your challenge for today is to create a program which is password protected,
and wont open unless the correct user and password is given.

For extra credit, have the user and password in a seperate .txt file.

for even more extra credit, break into your own program :)

'''
import itertools




name = 'rog'
pword = 'pwd'

# --program--------------------------------------
def encode(letter):
    ''' str -> str '''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    indx = alph.index(letter)
    shift = (indx - 3) % 26
    result = alph[shift]
    return result

def user_crack(strg):
    candidates = 'abcdefghijklmnopqrstuvwxyz'

    for p in (itertools.permutations(candidates, len(strg))):
        strng = ''
        for x in p:
            for letter in x:
                strng += letter

        if strng == name:
            print('name cracked! - ', strng)

        strng = ''
    return strng

def password_crack(strg):
    candidates = 'abcdefghijklmnopqrstuvwxyz'

    for p in (itertools.permutations(candidates, len(strg))):
        pw = ''
        for x in p:
            for letter in x:
                pw += letter

        if pw == pword:
            print('password cracked! - ', pw)

        pw = ''
    return pw

if __name__ == '__main__':

    choice = input('Input username/password or crack it? Enter user or crack  ')
    if choice == 'user':
        username = input('Username? ')
        password = input('Password? ')
        if username == name and password == pword:
            out = ''
            #message = 'retreat we are beat'
            message ='retreat'
            for letter in message:
                if letter.isalpha():
                    out += encode(letter)
                else:
                    out += ' '
            print('Message is {0} and when encrypted it is {1}'.format(message, out))

        else:
            print('Wrong password or username!')
    else:
        ans = user_crack(name)
        ans2 = password_crack(pword)
        if ans == 'rog' and ans2 == 'pwd':
            out = ''
            message ='retreat'
            for letter in message:
                if letter.isalpha():
                    out += encode(letter)
                else:
                    out += ' '
            print('Message is {0} and when encrypted it is {1}'.format(message, out))



# -------------------------------------------------------------------------------



