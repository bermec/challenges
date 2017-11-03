'''
Write a program that reads a matrix of numbers separated by newlines
 and whitespace, like this:

10 5 4 20
9 33 27 16
11 6 55 3

then calculates the sums for each row and column, optionally outputting them...

Rows: 39 85 75
Columns: 30 44 86 39

then prints two new matrices:

    first, print the matrix with its rows sorted by their sums
    then, print the matrix with its columns sorted by their sums.

Like this:

10 5 4 20
11 6 55 3
9 33 27 16

10 20 5 4
9 16 33 27
11 3 6 55

Here's a large input matrix to test your program on.

5 58 88 60 11 23 97 48 59 82 95 24 6 67 47
45 14 36 99 16 70 77 18 43 39 97 54 11 53 98
85 14 96 66 34 86 95 49 4 49 72 76 45 49 37
72 88 20 56 37 16 20 97 71 11 91 33 90 5 96
15 53 54 95 61 93 75 95 51 83 71 70 2 57 83
54 29 56 80 79 93 40 55 40 14 63 94 77 12 90
96 97 3 47 2 43 12 2 82 92 1 99 90 13 35
24 19 54 96 82 96 10 40 62 30 35 16 70 83 64
59 81 8 84 14 46 32 45 41 35 98 66 87 51 49
13 49 12 51 34 82 36 77 88 14 84 41 66 18 56
6 68 82 63 77 72 67 36 85 53 66 70 21 86 80
40 51 87 5 78 56 99 44 39 48 78 56 19 55 40
5 94 62 46 85 73 24 67 95 63 42 95 43 53 4
14 99 7 36 25 65 22 71 20 80 16 10 71 97 23
99 77 85 53 13 32 37 19 61 32 45 62 25 18 32
98 79 35 17 26 96 22 3 76 20 81 9 40 95 72
18 39 55 99 96 63 90 78 77 81 2 99 68 6 84
53 27 68 43 48 29 27 14 50 29 53 65 5 56 46
94 36 17 64 2 93 5 95 47 78 90 3 85 26 32
46 62 70 63 81 6 86 51 44 96 47 83 33 28 28

For bonus points, format your output matrices nicely
(align the columns, draw boxes with - and |...)

'''
import re

matrix = '''5 58 88 60 11 23 97 48 59 82 95 24 6 67 47
45 14 36 99 16 70 77 18 43 39 97 54 11 53 98
85 14 96 66 34 86 95 49 4 49 72 76 45 49 37
72 88 20 56 37 16 20 97 71 11 91 33 90 5 96
15 53 54 95 61 93 75 95 51 83 71 70 2 57 83
54 29 56 80 79 93 40 55 40 14 63 94 77 12 90
96 97 3 47 2 43 12 2 82 92 1 99 90 13 35
24 19 54 96 82 96 10 40 62 30 35 16 70 83 64
59 81 8 84 14 46 32 45 41 35 98 66 87 51 49
13 49 12 51 34 82 36 77 88 14 84 41 66 18 56
6 68 82 63 77 72 67 36 85 53 66 70 21 86 80
40 51 87 5 78 56 99 44 39 48 78 56 19 55 40
5 94 62 46 85 73 24 67 95 63 42 95 43 53 4
14 99 7 36 25 65 22 71 20 80 16 10 71 97 23
99 77 85 53 13 32 37 19 61 32 45 62 25 18 32
98 79 35 17 26 96 22 3 76 20 81 9 40 95 72
18 39 55 99 96 63 90 78 77 81 2 99 68 6 84
53 27 68 43 48 29 27 14 50 29 53 65 5 56 46
94 36 17 64 2 93 5 95 47 78 90 3 85 26 32
46 62 70 63 81 6 86 51 44 96 47 83 33 28 28'''

rows = []
column = []
columns = []
rows_sums=[]
column_sums = []

#-- convert matrix to list of lists ------------
matrix = matrix.split('\n')
for line in matrix:
    row = re.findall('\d+', line)
    int_row = []
    for item in row:
        int_row.append(int(item))
    rows.append(int_row)


#-- ROWS ---------------------------------

#-- sum rows and add to a list ----------
for row in rows:
    sum_row = sum(row)
    rows_sums.append(sum_row)
print('Rows: ', rows_sums)

#-- copy and sort row sums ---------
sorted_row_sums = rows_sums[::-1]
sorted_row_sums.sort()

#-- sort rows ------------------
output_rows = []
for num in sorted_row_sums:
    for row in rows:
        sum_of_row = sum(row)
        if sum(row) == num:
            output_rows.append(row)
            break

#- number to string ----------------------

rows_output = []
for row in output_rows:
    for num in row:
        rows_output.append(str(num))


chunks = [rows_output[x:x + len(row)] for x in range(0, len(rows_output), len(row))]

#print(chunks)

#-- print rows -----------------------------------
print('rows ')
for lst in chunks:
    print(*lst)

#-- columns ------------------------------------------------

print()
# iterate over rows, extract columns
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

#-- sum columns and add to list ----------
for column in columns:
    sum_column = sum(column)
    column_sums.append(sum_column)
print('Columns: ', column_sums)

#-- copy and sort column sums ---------
sorted_column_sums = column_sums[::-1]
sorted_column_sums.sort()

#-- sort columns ------------------
output_columns = []
for num in sorted_column_sums:
    for column in columns:
        if sum(column) == num:
            output_columns.append(column)
            break

column_output = sum(output_columns, [])

#- number to string ----------------------

col_output = []
for num in column_output:
    col_output.append(str(num))

#-- print columns ------------------------------
print()
cols = len(row)
lenl = len(col_output)
l = col_output
split = [l[i:i + int(lenl/cols)] for i in range(0, int(lenl), int(lenl / cols))]
print('columns')
for row in zip(*split):
    print("".join(str.ljust(i, 3) for i in row))


