a = ['1 2\n3 4', '5 6\n7 8']
b = ('5 6\n7 8')


print('{0:<10}{1:<10}'.format(a[0], a[1]))
#print('{} {}'.format(a[:4], b[:4]))
#print(a[:4])

#for i in n)[:-3]+'\n'for x in range(7)))

strings = ['1 2\n3 4', '5 6\n7 8']
#strings = ['string\none', 'string\ntwo', 'string\nthree']
#print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings])], sep='\n')