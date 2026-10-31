# Program to display numbers in reverse order

nums = map(int, input("Enter all the numbers: ").split())
nums = list(nums)
print("Reversed order:",end="")
for i in nums[::-1]:
    print(i,end=" ")
    