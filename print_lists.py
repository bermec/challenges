rows = [['1', '2', '3', '9', '10'], ['3', '4', '4', '9', '10'],['5', '6', '7', '9', '10']]
columns = []
column = []

acc = 0
for row in rows:
    len_row = len(row)
len_rows = len(rows)
while acc < len_row:

    for x in range(0, len(rows)):
        column.append(rows[x][acc])
    columns.append(column)
    column = []
    acc += 1
print(columns)