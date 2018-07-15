def check_score(score, *points):
    points = set(points)
    for x in range((score//min(points))+1):
        newpoints  = set()
        for a in points:
            if score % a == 0:
                print ("Valid Score")
                return
            for b in points:
                if a+b <= score:
                    newpoints.add(a+b)
        points = points.union(newpoints)

    print("Invalid Score")

check_score(234567890, 3,6,7,8)