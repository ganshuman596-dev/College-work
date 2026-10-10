'''Probem Statement: 3 vertices of the parallelogram are given (x1,y1), (x2,y2), (x3,y3).
   Assume the first point is the common vertex of the two sides.
   Find the fourth vertex.'''

x1, y1 = map(int, input("Enter the first coordinates(x1,y1): ").split())
x2, y2 = map(int, input("Enter the second coordinates(x2,y2): ").split())
x3, y3 = map(int, input("Enter the third coordinates(x3,y3): ").split())

x4 = x2+x3-x1 #by vector addition method
y4 = y2+y3-y1

print(f'The fourth vertex is: ({x4},{y4})')