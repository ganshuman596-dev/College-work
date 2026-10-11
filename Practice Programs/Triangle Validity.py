'''Problem Statement: Given three angles of a triangle, determine whether the angles form a
                      valid triangle or not.'''

a = float(input("Enter the first angle of the triangle: "))
b = float(input("Enter the second angle of the triangle: "))
c = float(input("Enter the third angle of the triangle: "))

if a+b+c==180:
    print("The angles entered can form a valid triangle.")
else:
    print("The angles entered cannot form a valid triangle.")
