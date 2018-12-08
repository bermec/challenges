import re

candidates = '''4 5 -1 -2 -7 2 -5 -3 -7 -3 1
-1 -6 -3 -7 5 -8 2 -8 1
-5 -1 -4 2 9 -9 -6 -1 -7'''

# prepare the strings
candidates_list = candidates.splitlines()
for candidates in candidates_list:
    candidates  = re.findall('[+-]?\d+', candidates)
    # create list of integer candidates
    candidates = list(map(int, candidates))
    # numerate into list of tuples for duplicate checking
    numerated_candidates = list(enumerate(candidates))

    sett = set()
    tuple_set = set()
    output = []
    print()
    for x in range(0, len(candidates)):
        for y in range(1, len(candidates)):
            sett.add(numerated_candidates[x][1])
            sett.add(numerated_candidates[y][1])
            if x == y:
                continue
            if numerated_candidates[y] in sett:
                continue
            # add the two selected  numbers
            first_two = numerated_candidates[x][1] + numerated_candidates[y][1]
            inverse = first_two * -1
            if inverse in candidates:
                if inverse in sett:
                    continue
                else:
                    # if correct....
                    ans = (numerated_candidates[x][1], numerated_candidates[y][1], inverse)
                    if inverse not in sett:
                        sort_ans = sorted(ans)
                        sort_ans = tuple(sort_ans)
                        if sort_ans not in tuple_set:
                            output.append((candidates[x], candidates[y], inverse))
                            tuple_set.add(sort_ans)
                            print(candidates[x], candidates[y], inverse)

            sett = set()



