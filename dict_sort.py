'''
sort dictionary by value

'''
import collections
d = {'John':5, 'Alex':10, 'Richard': 7}
Player = collections.namedtuple('Player', 'score name')


best = sorted([Player(v,k) for (k,v) in d.items()], reverse=True)

print(best)