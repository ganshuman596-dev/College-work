'''H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). 
Determine the angle (in degrees) of the hour hand on the clock face right now.'''

h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))

angle = (h*30)+(m*1/2)+(s*1/120)

print(f'The angle of hour hand is {angle} degrees')