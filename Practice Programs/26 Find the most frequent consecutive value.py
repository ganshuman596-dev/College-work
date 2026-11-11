'''Find the most frequent consecutive value: Accept the sequence of integer ending with -1.
   Determine which value occur in the longest consecutive run and print both the value and
   run length. If multiple values have same max run length, print the first search run.'''

print("Enter the sequence of integers one by one ending with -1")
max_num = None
prev = None
count = 0
max_count = 0
while True:
   i = int(input("Enter the integer: "))
   if i == -1:
      break
   if i == prev:
      count += 1
   else:
      prev = i
      count = 1
   if count > max_count:
      max_count = count
      max_num = i
print("Number occured maximum time:", max_num)
print("Runtime of maximum occured number:", max_count)
