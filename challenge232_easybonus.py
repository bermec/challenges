''' A two-word palindrome is (unsurprisingly) a palindrome that is two words long.
"Swap paws", "Yell alley" and "sex axes" (don't ask) are examples of this.

Using words from /r/dailyprogrammer's favorite wordlist enable1.txt,
how many two-word palindromes can you find? Note that just repeating
the same palindromic word twice (i.e. "tenet tenet") does not count
as proper two-word palindromes.
'''

def palinbonus(file):
    lst = []
    with open(file) as f:
        strng = ''
        acc = 0
        for line in f:
            line = line.strip()
            lst.append(line)
    return lst

def parse(lst):
    accum = 0
    strng = ''
    lst = palinbonus(lst)
    for x in range(0, len(lst)):
        slice = lst[x:x +2]
        for char in slice:
            strng += char
        if strng == strng[::-1]:
            accum += 1
        strng = ''
    return accum

if __name__ =='__main__':
    ans = parse('enable1.txt')
    print(ans)