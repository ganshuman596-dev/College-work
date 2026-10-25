'''Given integer coordinates of three vertices of a rectangle whose sides are parallel to the 
coordinate axes, find the coordinates of the fourth vertex of the rectangle. In the first test 
the three given vertices are (1, 4), (1, 6), (7, 4). The fourth vertex is thus (7, 6).'''

x1, y1 = map(int, input("Enter the coordiantes of first vertex(x1,y1): ").split())
x2, y2 = map(int, input("Enter the coordiantes of second vertex(x2,y2): ").split())
x3, y3 = map(int, input("Enter the coordiantes of third vertex(x3,y3): ").split())

if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

print(f'The coordinates of fourth vertex are: ({x4},{y4})')