# Program to calculate sum and average of first n numbers

n = int(input("Enter non-negative integer: "))
if n<0:
    print("Enter non-negative integer only!")
else:
    sum = 0
    for i in range(0,n+1):
        sum = sum+i
    print("Sum =", sum)
    if n==0:
        print("Average = 0")
    else:
        print("Average =", sum/n)