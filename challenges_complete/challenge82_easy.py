'''
Write a function that takes a number n as an argument and returns
(or outputs) every possible unique substrings (not counting "")
of the first n letters of the alphabet (in any order you like).
For example, substrings(5) could be:

a
ab
abc
abcd
abcde
b
bc
bcd
bcde
c
cd
cde
d
de
e

BONUS 1: Find a way to quickly determine how many strings this function
returns for a given input. If the alphabet were 500 letters long,
how much possible substrings would it have?

BONUS 2: Modify your function to take a string as an argument.
Make sure all substrings in your output are still unique (
i.e., there are two "l" substrings in "hello", but you should output only one).

'''

a = 'ab'
first =a[0:1]
print(first)
def substring(strng):
    output_list = []
    for x in range(0, len(strng)):
        for y in range(x + 1,len(strng) + 1):
            output = a[x:y]
            output_list.append(output)
    return output_list

if __name__ == '__main__':

    a = 'abcde'
    ans = substring(a)
    print(ans)

    #-- bonus 1 ------------------

    # formula n(n-1)/2
    N = 500
    ans = (N * (N - 1)) / 2
    print(ans)

    #-- bonus2 ------------------

    a = 'equation'
    ans = substring(a)
    print(ans)
