'''Find the angle between clock hands: Accept hours, minutes and seconds. Calculate the smaller
   angle between hour hand and minute hand, including the effect of seconds'''

h = int(input("Enter the hours: "))
m = int(input("Enter the minutes: "))
s = int(input("Enter the seconds: "))
h_angle  = 30*h + m/2 + s/120
m_angle = m*6 + s/10
angle = abs(h_angle-m_angle)
print(min(angle, 360-angle), "is the angle between clock hands")