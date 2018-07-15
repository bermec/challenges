stack = []
foo = ''
print("happy backwards math program! hit q to quit")
while foo != "q":
    # foo = input()
    foo_lst = [4, 2, '*']
    for x in range(0, len(foo_lst)):
        foo = foo_lst[x]
        try:
            stack.append(int(foo))
            print(stack)
        except ValueError:
            if foo in ["*","+","-","/"]:
                y = stack.pop()
                x = stack.pop()
                if foo == "*":
                    stack.append(x*y)
                if foo == "+":
                    stack.append(x+y)
                if foo == "-":
                    stack.append(x-y)
                if foo == "/":
                    stack.append(x/y)
                print(stack)

            else:
                print("broke")

    print("dat math!")