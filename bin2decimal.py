def bin2dec(n):
    store = 0
    x = 0
    # y = index of n
    for y in range(len(n) - 1, -1, -1):
        m = n[y]
        m = int(m)
        store += m * (2 ** x)
        x += 1
    return  store

if __name__ == '__main__':
    ans = bin2dec('111')
    print(ans)