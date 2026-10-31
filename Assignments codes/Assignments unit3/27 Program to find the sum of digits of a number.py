# Program to find the sum of digits of a number

num = input("Enter the number: ")
sum = 0
for i in num:
    sum = sum+int(i)
print("Sum of digits is =",sum)