'''
A number of sailors (let's call it N) are stranded on an island with a
huge pile of coconuts and a monkey. During the night, each sailor
(in turn) does the following without the others knowing:

    He takes one N'th (e.g. if N=5, one fifth) of the coconuts in the
    pile and hides them
    The division leaves one coconut left over, which is given to the
    monkey.

In the morning, they split the remaining coconuts between them. This
time the split is even. There's nothing left over for the monkey.

Your task: Given the number of sailors (N), how many coconuts were in
the pile to begin with (lowest possible number)?
'''

N = 5
ans = (N ** N - (N - 1))
print(ans)