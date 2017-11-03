def factors(n):
    lst = []
    for x in range(1, n):
        if n % x == 0:
            lst.append(x)
    return lst

def reduce_fraction(n, n2):
    temp = 0
    temp2 = 0

    master_lst = []
    master_lst2 = []
    lst1 = (factors(n))
    lst2 = (factors(n2))
    master_lst.extend(lst1)
    master_lst.extend(lst2)


    for items in master_lst:
        if items not in master_lst2:
            master_lst2.append(items)
    print(master_lst2)
    #master_lst2.remove(1)

    for x in range(0, len(master_lst2)):
        num = master_lst2[x]
        if n % num == 0 and n2 % num == 0:
            div = n / master_lst2[x]
            div2 = n2 / master_lst2[x]

            temp = div
            temp2 = div2

    return (int(div), int(div2))



if __name__ == '__main__':
    ans = factors(10 **3 - 1)
    print(ans)




