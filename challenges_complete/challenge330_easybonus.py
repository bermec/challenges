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

output picture
Bonus

For the bonus, we will rotate the axis for the bounding rectangle.
The first line of input will now be a vector determining the direction
of one edge of the bounding rectangle.
Bonus Input

1,1
1,1,2
2,2,0.5
-1,-3,2
5,2,1

Bonus Output

(-4.828, -2.000), (2.793, 5.621), (6.621, 1.793), (-1.000, -5.828)

'''
import re


def vector_values(t):
    vector_x = t[0]
    vector_y = t[1]
    # hypotenuse of vector
    vector_hypotenuse = (vector_x ** 2 + vector_y ** 2) ** 0.5
    # cos - adjacent / hypotenuse
    cos_theta = vector_x / vector_hypotenuse
    # sine - opposite / hypotenuse
    sin_theta = vector_y / vector_hypotenuse
    return cos_theta, sin_theta

# output pairs
def vector_points(x, y, sin_theta, cos_theta):
    vectorx = x * cos_theta - y * sin_theta
    vectory = y * sin_theta + x * cos_theta
    return vectorx, vectory


def two_d_rotate(x1, y1):
    x2 = x1 * cos_theta + y1 * sin_theta
    y2 = y1 * sin_theta - x1 * cos_theta
    return round(x2, 3), round(y2, 3)


candidates = '''1,1,2
2,2,0.5
-1,-3,2
5,2,1
'''
vector = 1, 1

vector_units = vector_values(vector)
sin_theta = vector_units[1]
cos_theta = vector_units[0]

candidates = candidates.splitlines()

xpos = []
ypos = []
radii = []

top_left = ()
for candidate in candidates:
    x_pos = re.findall('^[-+]?\d+', candidate)
    x_pos = x_pos[0]
    x_pos = float(x_pos)

    y_pos = re.findall(',([-+]?\d+),', candidate)
    y_pos = y_pos[0]
    y_pos = float(y_pos)
    radius = re.findall('\d+\.\d+$|\d+$', candidate)
    radius = float(radius[0])

    # rotate circle points
    x_and_y = vector_points(x_pos, y_pos, cos_theta, sin_theta)

    # pick points on the circles for reference
    xpos.append(x_and_y[0] - radius)
    xpos.append(x_and_y[0] + radius)
    ypos.append(x_and_y[1] - radius)
    ypos.append(x_and_y[1] + radius)

xmin = min(xpos)
xmax = max(xpos)

ymin = min(ypos)
ymax = max(ypos)

# rotate around the axis
east = two_d_rotate(xmin, ymin)
print(east)
north = two_d_rotate(float(xmin), float(ymax))
print(north)
west = two_d_rotate(float(xmax), float(ymax))
print(west)
south = two_d_rotate(float(xmax), float(ymin))
print(south)






