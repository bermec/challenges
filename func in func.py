def a(n):
    n += 2
    ans = b()
    return  ans

def b():
    return None

result = a(8)
print(result)