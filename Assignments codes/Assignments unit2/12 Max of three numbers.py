# Program to find maximun of three numbers

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a>b and a>c:
    max = a
elif b>a and b>c:
    max = b
else:
    max = c

print(f'{max} is maximum number')