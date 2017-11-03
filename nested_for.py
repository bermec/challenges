__author__ = 'rog'
for x in range(10):
    for y in range(10):
        for z in range(10):
            print(x,y,z)
            if x*y*z == 30:
                print("xyz break")
                break
        else:
            print("z continue")
            continue
        print("y break")
        break
    else:
        print("x continue")
        continue
    print("x break")
    break