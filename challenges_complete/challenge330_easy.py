'''
In this challenge, you will be given a set of circles, defined by their
centers and radii. Your goal is to find the bounding rectangle which
will contain all of the circles completely.

Write a program that determines the vertices of the bounding rectangle
with sides parallel to the axes.
Input Description

Each line will contain a comma separated center and radius for a circle.
Output Description

The format of the output will be comma separated coordinates, rounded
to 3 decimal places.
Challenge Input

1,1,2
2,2,0.5
-1,-3,2
5,2,1

input picture
Challenge Output

(-3.000, -5.000), (-3.000, 3.000), (6.000, 3.000), (6.000, -5.000)



'''
import re

candidates = '''1,1,2
2,2,0.5
-1,-3,2
5,2,1'''

candidates = candidates.splitlines()

xpos = []
ypos = []
radii = []

top_left = ()
for candidate in candidates:
    x_pos = re.findall('^[-+]?\d+', candidate)
    xpos.append(x_pos[0])
    y_pos = re.findall(',([-+]?\d+),', candidate)
    ypos.append(y_pos[0])
    radius = re.findall('\d+\.\d+$|\d+$', candidate)
    radii.append(radius[0])

xmin = min(xpos)
xmin_index = xpos.index(xmin)
xmax = max(xpos)
xmax_index = xpos.index(xmax)

ymin = min(ypos)
ymin_index = ypos.index(ymin)
ymax = max(ypos)
ymax_index = ypos.index(ymax)
ymax = float(ymax) + float(radii[ymax_index])

bottom_left = (float(xmin) - float(radii[xmin_index]), float(ymin) - float(radii[ymin_index]))
print(bottom_left)
top_left = (float(xmin) - float(radii[xmin_index]), float(ymax) + float(radii[ymax_index]))
print(top_left)
top_right = (float(xmax) + float(radii[xmax_index]), float(ymax) + float(radii[ymax_index]))
print(top_right)
bottom_right = (float(xmax) +float(radii[xmax_index]), float(ymin) - float(radii[ymin_index]))
print(bottom_right)


