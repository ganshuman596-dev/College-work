'''Find the longest strictly increasing fragment: Accept a sequence of integers ending with 0.
   Find the length of longest contigious fragment in which every number is strictly greater 
   than previous one.'''

print("Enter the sequence of integers ending with 0")
prev = None
count = 0
max_count = 0
while True:
   num = int(input("Enter the integer: "))
   if num == 0:
      break
   if num > prev and prev != None:
      count += 1
      prev = num
      if count > max_count:
         max_count = count
   else:
      count = 1
      prev = num
print("The max length is:", max_count)