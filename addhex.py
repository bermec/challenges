import itertools

def add_hex(A,B):
    A = "0"+A
    B = "0"+B
    #Remember all pattern include carry in variable d.
    i2h = dict(zip(range(16), "0123456789abcdef"))
    a = [(i,j) for i in "0123456789abcdef" for j in "0123456789abcdef"]
    b = list(map(lambda t: int(t[0],16)+int(t[1],16), a))
    c = ["0"+i2h[i] if i<16 else "1"+i2h[i-16] for i in b]#list of digit include carry
    d = dict(zip(a,c))#d={(digit,digit):digit,,,}
    #Calculate with variable d.
    result = ""
    cur = "0"
    nex = "0"
    for i in itertools.zip_longest(A[::-1], B[::-1], fillvalue = "0"):
        cur = d[(nex, d[i][1])][1]                   #cur = carry + digit + digit
        if d[i][0]=='1' or d[(nex, d[i][1])][0]=='1':#nex = carry = carry + digit + digit
            nex = "1"
        else:
            nex = "0"
        result += cur

    return result[::-1]

#Test
A = '10'
B = "10"
print(add_hex(A,B))
print(hex(int(A,16)+int(B,16)))#For validation

print(hex(0x69 ^ 0x69))# hex multiplication
print(hex(12 & 12))
print(hex(4356))
print(0x8 * 0x2)
print('dec to hex: ', hex(3314304900))
print('hex to dec: ', int('e0e2', 16))