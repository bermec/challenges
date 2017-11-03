import itertools

def morse(n):
    mm = []

    for dot in range(n+1):
        for dash in range(int(n/2)+1):
            if dot+dash*2 == n:
                t = ['.'] * dot + ['-']*dash
                for k in list(itertools.permutations(t)):
                    if k not in mm:
                        mm.append(k)

    for i in mm:
        print("".join(i))

    print(len(mm))

morse(10)