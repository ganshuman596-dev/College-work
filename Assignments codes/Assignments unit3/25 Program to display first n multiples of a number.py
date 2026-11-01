# Program to display first n multiples of a number

n = int(input("Enter the value of n: "))
num = int(input("Enter the number: "))

print(f'Following are the first {n} multiples of {num}: ',end="")
for i in range(1,n+1):
    print(num*i,end=" ")