# Program to find roots of the quadratic equation

import math
a = float(input("Enter the coefficient of quadratic term(a): ")) 
b = float(input("Enter the coefficient of linear term(b): ")) 
c = float(input("Enter the constant term(c): ")) 

d = (b**2)-(4*a*c)

if a == 0:
    print("It is not a quadratic equation.")
elif d>0:
    u = (-b + math.sqrt(d))/(2*a)
    v = (-b - math.sqrt(d))/(2*a)
    print(f'The solutions of quadratic equation are: {u} and {v}')
elif d==0:
    u = -b/(2*a)
    print(f'The equal roots of quadratic equation are: {u}')
else:
    print("No real roots")