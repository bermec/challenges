a = '123'
x = 0
while True:
    slice = a[x:x + 2]

    if int(slice) > 27:
        print('too big')
        x += 1
        break
    print(slice)
    x += 2


#print(slice)

    

