parent = {}
level = {}


def BFS(s, Adj):
    level[s] = 0
    parent[s] = None
    i = 1
    frontier = [s] # level i - 1
    while frontier:
     next = [] # level i
     for u in frontier:
       for v in Adj[u]: # edge from u to v
         if v not in level:
           level[v] = i
           parent[v] = u
           next.append(v)
     frontier = next
     i += 1

vertices = ["s", "a", "c", "d", "f", "z", "x", "v"]
adjacency_list = {
   "a": ["s", "z"],
   "z": ["a"],
   "s": ["a", "x"],
   "x": ["s", "d", "c"],
   "d": ["x", "c", "f"],
   "c": ["x", "d", "f", "v"],
   "f": ["d", "c", "v"],
   "v": ["c", "f"]}

ans = BFS("s", adjacency_list)
print(ans)

'''
1  parent = {}
2  level = {}
3
4  def BFS(s, Adj):
5    level[s] = 0
6    parent[s] = None
7    i = 1
8    frontier = [s] # level i - 1
9    while frontier:
10     next = [] # level i
11     for u in frontier:
12       for v in Adj[u]: # edge from u to v
13         if v not in level:
14           level[v] = i
15           parent[v] = u
16           next.append(v)
17     frontier = next
18     i += 1
19
20 vertices = ["s", "a", "c", "d", "f", "z", "x", "v"]
21 adjacency_list = {
22   "a": ["s", "z"],
23   "z": ["a"],
24   "s": ["a", "x"],
25   "x": ["s", "d", "c"],
26   "d": ["x", "c", "f"],
27   "c": ["x", "d", "f", "v"],
28   "f": ["d", "c", "v"],
29   "v": ["c", "f"]
30 }
31
32 BFS("s", adjacency_list) '''