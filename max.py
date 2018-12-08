'''
Description

This challenge is about finding minimums/maximums. The challenge consists
of two similar word problems where you will be asked to maximize/minimize
a target value.

To make this more of a programming challenge rather than using programming
as a calculator, I encourage you to try to find a generic minimize/maximize
function rather than just calculating the answer directly.
Challenge

    A piece of wire 100 cm in length is bent into the shape of a sector of a
    circle. Find the angle of the sector that maximizes the area A of the s
    ector. sector_image

    A and B are towns 20km and 30km from a straight stretch of river 100km
    long. Water is pumped from a point P on the river by pipelines to both
    towns. Where should P be located to minimize the total length of pipe
    AP + PB? river_image

Challenge Outputs

The accuracy of these answers will depending how much precision you use
when calculating them.

    ~114.6

    ~40
'''
radius = 0
max_area = 0
theta_dict = {}
P = 100
theta = 0
while theta <= 101:
    r = (P - theta) / 2
    A = (theta * r) / 2
    if A >= max_area:
        max_area = A
        theta_dict['theta'] = theta
        radius = r
    theta += 0.1

print(theta_dict['theta'], r)