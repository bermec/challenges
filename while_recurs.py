'''
def ispal_iterative(N):
    hw = 1
    while N:
        bits = N.bit_length()
        N -= 2**(bits-1)
        hw *= 2
    return hw '''
'''
def ispal(N):
    hw = 1
    while N:

    return hw
'''
def ispal(N, acc):

    if acc == 3:
        return [1]

    else:
        L = ispal(N, acc)
        L.extend([2*i for i in L])
        acc += 1
        return L

if __name__ == '__main__':
    ans = ispal(16,0)
    print(ans)