def draw(width,hight,directions):
    a = []
    up = 0
    right = 0
    b = ' '*width
    for i in range(hight):
        a.append(b)
    directions = directions.lower()
    for i in directions:
        if i == 'n': up-=1
        elif i == 's': up+=1
        elif i == 'e': right+=1
        elif i =='w': right -=1
        elif i == 'p':
            newline = a[up][:right]+'*'+a[up][right+1:]
            a = a[:up]+[newline]+a[up+1:]
        newline = b
    return '\n'.join(a)

if __name__ == '__main__':

    width = 5
    height = 5
    directions = 'PESPESPESPESPNNNNPWSPWSPWSPWSP'
    ans = draw(width, height, directions)
    print(ans)