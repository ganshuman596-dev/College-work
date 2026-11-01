'''Problem Statement: Given Hours, Minutes, Seconds.
   Calculate angle of minute hand from 12'o clock position.'''

h = int(input("Enter the hours: "))
m = int(input("Enter the minutes: "))
s = int(input("Enter the seconds: "))

angle = (m*6)+(s*1/10)

print(f'The angle of minute hand is = {angle}')