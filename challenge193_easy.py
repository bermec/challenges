''' An international shipping company is trying to figure out
how to manufacture various types of containers. Given a volume
they want to figure out the dimensions of various shapes that
would all hold the same volume.
Input:

A volume in cubic meters.
Output:

Dimensions of containers of various types that would hold the volume.
The following containers are possible.

    Cube
    Ball (Sphere)
    Cylinder
    Cone

Example Input:

27
Example Output:

 Cube: 3.00m width, 3.00m, high, 3.00m tall
 Cylinder: 3.00m tall, Diameter of 3.38m
 Sphere: 1.86m Radius
 Cone: 9.00m tall, 1.69m Radius

Some Inputs to test.

27, 42, 1000, 2197
'''

import math

def cube(vol):
    r = vol / 3
    return r

def sphere(vol):
    r = ((3 * vol) / (4 * math.pi)) ** (1 / 3)
    r = round(r, 2)
    return r

def cylinder(vol):
    r = (vol / (math.pi * h)) ** 0.5
    r = round(r, 2)
    return r

def cone(vol):
    r = (3 * (vol / (math.pi * h))) ** 0.5
    r = round(r, 2)
    return r

def display(volume, h):
    print('A cube of {0} metres cubed will have sides of {1} metres'.format(volume, h))
    print('A sphere of volume {0} cubic metres will have a radius of {1} metres.'.format(volume, sphere(volume)))
    print('A cylinder of {0} cubic metres with a height of {1} will have a radius of {2} metres.'.format(volume, h, cylinder(volume)))
    print('A cone of {0} cubic metres and height of {1} metres will have a radius of {2} metres'.format(volume, h, cone(volume)))


if __name__ == '__main__':

    lst = [27, 42, 1000, 2197]
    for num in lst:
        h = round((num / 9), 2)
        display(num, h)
        print()

