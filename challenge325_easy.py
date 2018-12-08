def path_check(maze, x, y, code_num,):
    '''Check if there is a null route
    by running a further move, no
    cache collection would be the
    result.'''
    cache = []
    code_num += 1
    code_index = code_num % 5
    target = code_list[code_index]
    up = step_up(maze1, x, y)
    if up[0] == target:
        cache.append((x, y - 1))
    down = step_down(maze1, x, y)
    if down[0] == target:
        cache.append((x, y + 1))
    left = walk_left(maze1, x, y)
    if left[0] == target:
        cache.append((x - 1, y))
    right = walk_right(maze1, x, y)
    if right[0] == target:
        cache.append((x + 1, y))
    if len(cache) == 0:
        return False
    else:
        return True


def walk_left(maze, x, y):
    if x - 1 == -1:
        return ' '
    ans = maze[y][x - 1]
    return ans, y, x - 1


def walk_right(maze, x, y):
    if x + 1 == -1 or x > len(maze1):
        return ' '
    ans = maze[y][x + 1]
    return ans, y, x + 1


def step_up(maze, x, y):
    if y - 1 == -1:
        return ' '
    ans = maze[y - 1][x]
    return ans, y - 1, x


def step_down(maze, x, y):
    if y + 1 == -1:
        return ' '
    ans = maze[y + 1][x]
    return ans, y + 1, x



if __name__ == '__main__':

    candidates = '''R R B R R R B P Y G P B B B G P B P P R
    B G Y P R P Y Y O R Y P P Y Y R R R P P
    B P G R O P Y G R Y Y G P O R Y P B O O
    R B B O R P Y O O Y R P B R G R B G P G
    R P Y G G G P Y P Y O G B O R Y P B Y O
    O R B G B Y B P G R P Y R O G Y G Y R P
    B G O O O G B B R O Y Y Y Y P B Y Y G G
    P P G B O P Y G B R O G B G R O Y R B R
    Y Y P P R B Y B P O O G P Y R P P Y R Y
    P O O B B B G O Y G O P B G Y R R Y R B
    P P Y R B O O R O R Y B G B G O O P B Y
    B B R G Y G P Y G P R R P Y G O O Y R R
    O G R Y B P Y O P B R Y B G P G O O B P
    R Y G P G G O R Y O O G R G P P Y P B G
    P Y P R O O R O Y R P O R Y P Y B B Y R
    O Y P G R P R G P O B B R B O B Y Y B P
    B Y Y P O Y O Y O R B R G G Y G R G Y G
    Y B Y Y G B R R O B O P P O B O R R R P
    P O O O P Y G G Y P O G P O B G P R P B
    R B B R R R R B B B Y O B G P G G O O Y'''



    # prepare the maze
    maze1 = []
    maze = candidates.splitlines()
    for line in maze:
        line = line.replace(' ', '')
        line = line.strip()
        maze1.append(line)


    cache = []
    code_list = ['R', 'O', 'Y', 'P', 'O']
    code_num = 0
    code_index = code_num%5
    target = code_list[code_index]
    n = len(maze1)
    path = []
    candidate_list = {}

    # starting move, initial 'R'
    for y in range(n - 1, -1, -1):
        for x in range(0, n):
            if y == n - 1:
                # initial target and co-ords
                temp = maze1[y][x]
                if temp == target:
                    # if this is the target, add it to the path.
                    path.append((x, y, target))
                    # code number advances to give next target, 'O'
                    code_num += 1
                    code_index = code_num % 5
                    target = code_list[code_index]
                    # go up looking for the target
                    up = step_up(maze1, x, y)
                    # add to cache
                    cache.append((x,y - 1))
                    # if not the target continue to next x
                    if not up[0] == target:
                        code_num -= 1
                        code_index = code_num % 5
                        target = code_list[code_index]
                        path = []
                        cache = []
                        continue
                    else:
                        # if target correct
                        path.append((cache[0], target))
                        x = cache[0][0]
                        y = cache[0][1]
                        # reset cache
                        cache = []
                        while True:
                            code_num += 1
                            code_index = code_num % 5
                            target = code_list[code_index]
                            up = step_up(maze1, x, y)
                            if up[0] == target:
                                cache.append((x,y - 1))
                            down = step_down(maze1, x, y)
                            if down[0] == target:
                                cache.append((x,y + 1))
                            left = walk_left(maze1, x, y)
                            if left[0] == target:
                                cache.append((x - 1, y))
                            right = walk_right(maze1, x, y)
                            if right[0] == target:
                                cache.append((x + 1, y))
                            if len(cache) == 0 and y == 1:
                                print(path)
                                exit()
                            if len(cache) == 1:
                                path.append((cache[0], target))
                                x = cache[0][0]
                                y = cache[0][1]
                                cache = []
                            else:
                                x = cache[0][0]
                                y = cache[0][1]
                                if y >= cache[1][1]:
                                    x = cache[1][0]
                                    y = cache[1][1]
                                    cache = []
                                path_chk = path_check(maze1, x, y, code_num)
                                # note: test smallest 'Y' for shortest route
                                if path_chk:
                                    path.append((cache[0], target))
                                    x = cache[0][0]
                                    y = cache[0][1]
                                    cache = []
                                else:
                                    x = cache[1][0]
                                    y = cache[1][1]
                                    path.append((cache[1], target))
                                    cache = []
                                if y == 0:
                                    print(path)
                                    exit()



