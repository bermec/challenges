import re

strng = '''Summary
entry 1
Start Date
08/02/17 00:00
End Date
10/02/17 00:00

Summary
entry 2
Start Date
07/02/17 00:00
End Date
10/02/17 00:00

Summary
entry 3
Start Date
21/02/17 00:00
End Date
25/02/17 00:00'''

lst = []

for line in strng.splitlines():
    line = line.strip()
    entries = re.findall('^\w+\s\d', line)
    if entries:
        lst.append(entries)
print(lst)