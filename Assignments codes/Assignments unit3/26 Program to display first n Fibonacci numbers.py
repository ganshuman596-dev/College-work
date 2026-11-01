# Program to display first n Fibonacci numbers

n = int(input("Enter the integer greater than 0: "))
a = 0
b = 1
for i in range(n+1):
    print(a,end=" ")
    a,b = b,a+b