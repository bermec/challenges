def titlecase(s, ex):
    output = ''
    strng = s.split()
    for word in strng:
        if word not in ex:
            output += word.capitalize() + ' '
        else:
            output += word + ' '
    return output


if __name__ == '__main__':
    exceptions = ['jumps', 'the', 'over']
    ans = titlecase('the quick brown fox jumps over the lazy dog', exceptions)
    print(ans)