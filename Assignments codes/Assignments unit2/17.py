'''Given a sequence of integer numbers ending with the number 0. Determine the length of 
the widest fragment where all the elements are equal to each other.'''

seq = []
while True:
    element = int(input("Enter the integer and 0 for end: "))
    seq.append(element)
    if element == 0:
        break

max_count = 0
count = 0
previous = None
for i in seq:
    if i == 0:
            break
    if i == previous:
        count += 1
    else:
        count == 0
    if count>max_count:
         max_count = count

print(f'The largest fragement is of {max_count} integers')
    