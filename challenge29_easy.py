''' A Palindrome is a sequence that is the same in reverse as it is forward.

I.e. hannah, 12321.

Your task is to write a function to determine whether a given string is palindromic or not.

Bonus: Support multiple lines in your function to validate Demetri Martin's 224 word palindrome poem.

'''

def isPalindrome(strng):
    ''' str -> bool
    '''
    if strng == strng[::-1]:
        return True
    else:
        return  False

if __name__ == '__main__':

    sample = isPalindrome('hannah')
    print(sample)

    sample= ''
    #with open('224palindrome.txt') as f:
    with open('palintest.txt', 'r') as f:
        for line in f:
            line.split()
            line = line.strip()
            for item in line:
                if item.isalnum():
                    sample += item

    poem = isPalindrome(sample)
    print(poem)