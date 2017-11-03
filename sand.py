sand = '.';
stone = '#';
space = ' ';
lines = []
# Read in n and lines
n = int(input('lines?  '))
s = str(input('sand?'))
s.ljust(n)
lines.append(list(s))

# Loop from bottom to top
for i in range(n-1, -1, -1):
  for j in range(n-1, -1, -1):
    piece = lines[i][j]
    if (piece == space) or (piece == stone):
      continue

    k = i
    while (k < n-1):
      nextPiece = lines[k+1][j]
      if (nextPiece == stone) or (nextPiece == sand):
        break
      k = k+1

    lines[i][j] = space
    lines[k][j] = sand

output = "";
for line in lines:
  output += ''.join(line) + '\n'

print(output)