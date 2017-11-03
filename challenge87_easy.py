'''
Write a function that calculates the intersection of two rectangles,
returning either a new rectangle or some kind of null value.

You're free to represent these rectangles in any way you want:
tuples of numbers, class objects, new datatypes, anything goes. For
this challenge, you'll probably want to represent your rectangles
as the x and y values of the top-left and bottom-right points.
(Rect(3, 3, 10, 10) would be a rectangle from (3, 3) (top-left) to
(10, 10) (bottom-right).)

As an example, rectIntersection(Rect(3, 3, 10 10), Rect(6, 6, 12, 12))
would return Rect(6, 6, 10, 10), while rectIntersection
(Rect(4, 4, 5, 5), Rect(6, 6, 10 10)) would return null.

'''

'''
Based on:
A.X1 < B.X2: 	true
A.X2 > B.X1: 	false
A.Y1 < B.Y2: 	true
A.Y2 > B.Y1: 	true
Intersect: 	false'''

def intersect(rect1, rect2):
    if (rect1[0] < rect2[2]) and rect1[2] > rect2[0] and \
                    rect1[1] < rect2[3] and rect1[3] > rect2[1]:
        rectangle = (rect2[0], rect2[1], rect1[2], rect1[3])
        return 'rectangle ' + str(rectangle)
    else:
        return 'no intersect!'


if __name__ == '__main__':
    rect_one = (3, 3, 10, 10)
    rect_two = (6, 6, 12, 12)
    ans = intersect(rect_one, rect_two)
    print(ans)
