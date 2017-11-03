def convert(l, N):
    '''shorten list of tuples to list of lists
    of sum eight '''
    lst2 = []
    output_list = []
    for tup in l:
        lst2 = []
        for element in tup:
            while sum(lst2) < N:
                lst2.append(element)
                break
        if sum(lst2) == 4:
            output_list.append(lst2)
    return output_list

if __name__ == '__main__':
    N = 4
    lst =[[1, 2, 1, 2],[2, 1, 2, 1]]
    ans = convert(lst, N)
    print(ans)