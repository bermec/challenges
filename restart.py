
should_restart = True
while should_restart:
    should_restart = False
    for i in range(10):
        print(i)
        if i == 5:
            should_restart = True
            break