import math
shape = int(input("Enter 1 for area of circle and 2 for triangle: "))
if shape == 1:  #For circle
    r = float(input("Enter the radius of circle: "))
    area = math.pi*(r**2)
    print(f'The area of circle is {area} units')
else:  #For triangle
    h = float(input("Enter the height of triangle: "))
    b = float(input("Enter the base of triangle: "))
    area = 0.5*h*b
    print(f'The area of triangle is {area} units')