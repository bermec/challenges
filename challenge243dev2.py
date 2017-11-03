lis = [9, 111, 21 ]

for i in range(0, len(lis)):
    new_lis = []
    new_lis.append(lis[i])
    for j in range(1,lis[i]//2 +1):
        if lis[i] % j == 0:
            new_lis.append(j)

    total = sum(new_lis)
    if total < 2 * lis[i]:
        msg =  "%d deficient" % lis[i]
    elif total > 2 * lis[i]:
        msg = "%d abundant by %d" % (lis[i], total - 2* lis[i])
    else:
        msg = lis[i], "~~neither~~ deficient"
    print(msg)