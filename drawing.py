ledsperline = 3
total_lines = 8
led = '-|>|-'
link = '-'
para = '|'
star = '*'
line = star + link + (led + link) * ledsperline + star
print(line)

line_next = ' ' + link + (led + link) * ledsperline

for x in range(0, total_lines - 1):
    spacer = ' ' + para.ljust(len(line_next) - 2, ' ') + para
    print(spacer)
    print(line_next)
