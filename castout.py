def CastOut(Base=10, Start=201, End=9000):
    ran = [y for y in range(Base - 1) if y % (Base - 1) == (y * y) % (Base - 1)]
    x, y = divmod(Start, Base - 1)
    while True:
        for n in ran:
            k = (Base - 1) * x + n
            if k < Start:
                continue
            if k > End:
                return
            yield k
        x += 1


for V in CastOut(Base=10, Start=2, End=90):
    print(V, end=' ')

Base = 10
N = 6
Paddy_cnt = 1
for n in range(N):
    for V in CastOut(Base, Start=Base ** n, End=Base ** (n + 1)):
        for B in range(n + 1, n * 2 + 2):
            x, y = divmod(V * V, Base ** B)
            if V == x + y and 0 < y:
                print('{1}: {0}'.format(V, Paddy_cnt))
                Paddy_cnt += 1
                break