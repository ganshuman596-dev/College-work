'''Problem Statement: Given Hours, Minutes, Seconds.
   Calculate angle of hour hand from 12'o clock position.'''

h = int(input("Enter the hours: "))
m = int(input("Enter the minutes: "))
s = int(input("Enter the seconds: "))

angle = (h*30)+(m*1/2)+(s*1/120)

print(f'The Angle of Hour hand is = {angle}')