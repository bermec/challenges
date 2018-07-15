if __name__ == '__main__':
    import re

    data = '''.....................................
    ...#######################...........
    ...#.....................#...........
    ...#.....................#...........
    ...#.....................#...........
    ...#.....................#...........
    ...#.....................#...........
    ...#.....................#######.....
    ...###.................##......#.....
    ...#..##.............##........#.....
    ...#....##.........##..........#.....
    ...#......##.....##............#.....
    ...#........#####..............#.....
    ...#........#..................#.....
    ...#.......##..................#.....
    ...#.....##....................#.....
    ...#...##......................#.....
    ...#############################.....
    .....................................
    .....................................
    .....................................
    .....................................
    8 12 @'''

    if __name__ == '__main__':
        import re

        data = '''.....................................
        ...#######################...........
        ...#.....................#...........
        ...#.....................#...........
        ...#.....................#...........
        ...#.....................#...........
        ...#.....................#...........
        ...#.....................#######.....
        ...###.................##......#.....
        ...#..##.............##........#.....
        ...#....##.........##..........#.....
        ...#......##.....##............#.....
        ...#........#####..............#.....
        ...#........#..................#.....
        ...#.......##..................#.....
        ...#.....##....................#.....
        ...#...##......................#.....
        ...#############################.....
        .....................................
        .....................................
        .....................................
        .....................................
        8 12 @'''

        data = data.splitlines()

        for line in data:

            sample = re.findall(r'(?<=\.\#)((\.+)(?=\#+\.+\#+\.+))', line)

            if len(sample) > 0:
                N = len(sample[0][0])
                line2 = re.sub(r'(?<=\.\#)((\.+)(?=\#+\.+\#+\.+))', '@' * N, line)
                print(line2)
            else:
                print(line)