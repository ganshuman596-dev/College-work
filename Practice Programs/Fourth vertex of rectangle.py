'''Probem Statement: 3 vertices of the rectangle are given (x1,y1), (x2,y2), (x3,y3).
   Assume the first point is the common vertex of the two sides.
   Find the fourth vertex.'''

x1, y1 = map(int, input("Enter the coordinates of first point (x1,y1): ").split())
x2, y2 = map(int, input("Enter the coordinates of second point (x2,y2): ").split())
x3, y3 = map(int, input("Enter the coordinates of third point (x3,y3): ").split())

if x1 == x2:   #finding common x coordinate
    x4 = x3 
elif x1 == x3:
    x4 = x2 
else:
    x4 = x1

if y1 == y2:   #finding common y coordinate
    y4 = y3 
elif y1 == y3:
    y4 = y2 
else:
    y4 = y1

print(f'The coordinates of fourth vertex are: ({x4},{y4})')