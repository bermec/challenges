class Found(Exception): pass
try:
    for i in range(10):
        for j in range(5):
            for k in range(2):
               if i + j + k == 12:
                  raise Found
except Found:
    print(i, j, k)