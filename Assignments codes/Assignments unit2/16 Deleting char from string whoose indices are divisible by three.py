# Given a string. Delete from it all the characters whose indices are divisible by three.

s = input("Enter the string:")

new_s = ""
for i,a in enumerate(s):
    if i%3!=0:
        new_s = new_s + a

print(f'The modified string is: {new_s}')