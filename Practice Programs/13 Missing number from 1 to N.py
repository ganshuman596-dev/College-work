'''Problem Statement: A set contains numbers from 1 to N.
   One number is missing.
   Write a program to find the missing number.'''

n = int(input("Enter the value of N: "))
nums_available = map(int, input("Enter the number available: ").split())
missing = (n*(n+1)/2) - sum(nums_available)

print(f'The missing number is: {int(missing)}')