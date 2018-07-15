'''
Given a well-formed (non-empty, fully valid) string of digits,
let the integer N be the sum of digits. Then, given this integer N,
turn it into a string of digits. Repeat this process until you
only have one digit left. Simple, clean, and easy: focus on
writing this as cleanly as possible in your preferred programming
languauge.
'''

def recursum(strng):
    strng = str(strng)
    if len(strng) == 1:
        return strng
    else:
        strng = sum(int(d) for d in strng.strip())
        return recursum(strng)

if __name__ == '__main__':
    strng = '123456'
    ans = recursum(strng)
    print(ans)