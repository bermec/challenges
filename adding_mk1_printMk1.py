a = 'Fred'
if a.startswith(('D', 'G', 'F')):
    print(True)

if any(map(a.startswith, ('D', 'G', 'F'))):
    print('True!')