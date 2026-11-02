'''Delete the character at prime number indices: Accept a string and remove all 
   the characters whose indices are prime number. Use 0 based indexing and do not use 
   external libraries'''

string = input("Enter the string: ")
new = list(string)

for i in range(len(string)-1, 1, -1):
    if i>1:
        for x in range(2,i):
            if i%x==0:
                break
        else:
            new.pop(i)
print("New string:", "".join(new))