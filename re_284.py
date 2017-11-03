import re

def candidates(string):
    with open("enable1.txt") as words:
        for word in words:
            if len(word) > 5:
                pattern = "^" + ".*".join(word[:-1]) + "$"
                if re.search(pattern, string):
                    yield word[:-1]

if __name__ == '__main__':

    strng = 'qwertyuytresdftyuioknn'
    ans = candidates(strng)
    print(next(ans))