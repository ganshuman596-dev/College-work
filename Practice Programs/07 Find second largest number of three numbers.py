'''Find the second largest of three numbers: Write a python program to accept 3 distinct numbers
   and print the second largest number, without using sort() function or max() function'''

a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = int(input("Enter the first number: "))

if (a>b and a<c) or (a<b and a>c):
    print(a, "is second largest number")
elif (b>a and b<c) or (b<a and b>c):
    print(b, "is second largest number")
else:
    print(c, "is second largest number")
