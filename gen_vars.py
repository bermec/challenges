import random

N = 4
sqrN = N ** 2

# numbers to use for 'random rain'
acc = 0
for x in range(N, sqrN+1, N):
    print(x)
    acc += N

print()

# sand and brick indexes
acc = N
while acc < sqrN:
    num = (random.randrange(N)) + acc - 1
    print(num)
    acc += N
