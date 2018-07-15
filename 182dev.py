
def sentence(N, l):
    ''' list -> list
    return 25 length sections'''
    lst =[]
    b = ''
    x = 0
    while True:

        try:
            temp = len(b) + 1 + len(l[x])
            if temp <= N:
                b += l[x] + ' '
                x += 1
            else:
                delme = len(b)
                # top up with spaces if required.
                while len(b) < N:
                    b += ' '
                lst.append(b)
                b = ''
        except IndexError:
            lst.append(b)
            return lst


if __name__ == "__main__":
    import re
    format_style = [4, 25, 1]
    lst = []
    N = 25
    # prepare text as one complete string
    with open('loren_ipsum.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            lst.append(line)

        lst = ' '.join(lst)
        lst = lst.split()
        # build sentences here
        lsts = sentence(N, lst)

    #build four columns in layers
    output = []
    layer = ''
    x = 0
    y = x
    while y < 10:
        len_lsts = len(lsts)
        temp = lsts[x]
        layer += lsts[x] + ' '
        x += 10
        layer += lsts[x] + ' '
        x += 10
        layer += lsts[x] + ' '
        x += 10
        layer += lsts[x] + ' '
        output.append(layer)
        layer = ''
        y += 1
        x = y

    for strng in output:
        print(strng)


