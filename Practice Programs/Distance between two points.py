'''Problem Statement: Given two points (x1,y1) and (x2,y2).
                      Calculate the distance between them.'''

x1, y1 = map(int, input("Enter the first point(x1,y1): ").split())
x2, y2 = map(int, input("Enter the second point(x2,y2): ").split())

dist = ((x1-x2)**2+(y1-y2)**2)**(1/2)

print(f'The distance given two points is: {dist} units')