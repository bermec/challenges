''' Implement Dijkstra's algorithm in any way you can :)
'''

#-- nodes ------------------
a = 0
b = 1000
c = 1000
d = 1000
e = 1000
# -- dict of edge paths -----------
dikt = {}
dikt['ab'] = 2
dikt['ac'] = 4
dikt['bd'] = 3
dikt['cd'] = 6
dikt['ce'] = 6
dikt['de'] = 3
print(dikt)

#-- list of nodes -------------------------
lst =[a, b, c, d, e]
#-- starting node is a ----------------------------------------------
#-- find edges that connect to node a  and update values of nodes ---
for key, value in dikt.items():
    if key.startswith('a') and key.endswith('b'):
        b = min(b,(a + value))
    elif key.startswith('a') and key.endswith('c'):
        c = min(c,(a + value))
    elif key.startswith('b') and key.endswith('d'):
        d = min(d,(b + value))
    elif key.startswith('c') and key.endswith('d'):
        d = min(d,(c + value))
    elif key.startswith('c') and key.endswith('e'):
        e = min(e,(c + value))
    elif key.startswith('d') and key.endswith('e'):
        e = min(e,(d + value))

#-- update node list -----
lst =[a, b, c, d, e]
print(' lst: ', lst)
a = 1000
lst = [a, b, c, d, e]
#-- find lowest node left ------------
#-- extract the next node ---------
lo_node = min(lst)
print(lo_node)
if lo_node == a:
    a = lo_node
elif lo_node == b:
    b = lo_node
    for key, value in dikt.items():
        if key.startswith('b') and key.endswith('c'):
            c = min(d,(b + value))
        elif key.startswith('b') and key.endswith('d'):
            d = min(d,(b + value))
        elif key.startswith('b') and key.endswith('e'):
            e = min(e,(b + value))
elif lo_node == c:
    c = lo_node
    for key, value in dikt.items():
        if key.startswith('c') and key.endswith('d'):
            d = min(d,(c + value))
        elif key.startswith('c') and key.endswith('e'):
            e = min(e,(c + value))
elif lo_node == d:
    d = lo_node
    for key, value in dikt.items():
        if key.startswith('d') and key.endswith('c'):
            c = min(c,(d + value))
        elif key.startswith('d') and key.endswith('e'):
            e = min(e,(d + value))
else:
    lo_node == e
    e = lo_node

#-- update lst -----------------------------
lst =[a, b, c, d, e]
print(lst)
b  = 1000
lst = [a, b, c, d, e]
print(lst)
#-- pick lowest value in list -----------------------
lo_node = min(lst)
print(lo_node)
if lo_node == a:
    a = lo_node
elif lo_node == b:
    b = lo_node
    for key, value in dikt.items():
        if key.startswith('b') and key.endswith('d'):
            d = min(d,(b + value))
        elif key.startswith('b') and key.endswith('e'):
            d = min(d,(c + value))
elif lo_node == c:
    c = lo_node
    for key, value in dikt.items():
        if key.startswith('c') and key.endswith('d'):
            d = min(d,(c + value))
        elif key.startswith('c') and key.endswith('e'):
            e = min(e,(c + value))
else:
    lo_node == d
    d = lo_node

lst = [a, b, c, d, e]
print(lst)
#-- now check b -------------------------

#-- pick lowest value in list -----------------------
lo_node = min(lst)
print(lo_node)
if lo_node == a:
    a = lo_node
elif lo_node == b:
    b = lo_node
    for key, value in dikt.items():
        if key.startswith('b') and key.endswith('d'):
            d = min(d,(b + value))
        elif key.startswith('b') and key.endswith('e'):
            d = min(d,(c + value))
elif lo_node == c:
    c = lo_node
    for key, value in dikt.items():
        if key.startswith('c') and key.endswith('d'):
            d = min(d,(c + value))
        elif key.startswith('c') and key.endswith('e'):
            d = min(d,(c + value))
else:
    lo_node == d
    d = lo_node
b = 1000
lst = [a, b, c, d, e]
print(lst)
print('The shortest route between node a and node e is {0} units.'.format(lst[-1]))