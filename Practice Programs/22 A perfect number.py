'''A perfect number: A perfect equals the sum of its positive divisor excluding itself.
   Accept an integer and determine whether its perfect.'''

num = int(input("Enter the positive integer: "))
chk_sum = 0
for i in range(1, num):
    if num%i==0:
        chk_sum = chk_sum+i
if chk_sum == num:
    print(num, "is perfect number!")
else:
    print(num, "is not perfect number!")
