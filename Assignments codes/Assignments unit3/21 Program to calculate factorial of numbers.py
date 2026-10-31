# Program to calculate factorial of numbers

n = int(input("Enter the number: "))

if n == 0:
    factorial = 0
    print("Factorial of 0 is 0")
elif n<0:
    print("Enter non-negative number only!")
else:
    factorial = 1
    for i in range(2,n+1):
        factorial = factorial*i
    print(f'Factorial of {n} is {factorial}')