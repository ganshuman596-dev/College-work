'''A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, 
calculate how many seconds is between them. The moment of the first timestamp occurred before the 
moment of the second timestamp.'''

h1 = int(input("Enter the hours of first timestamp: "))
m1 = int(input("Enter the minutes of first timestamp: "))
s1 = int(input("Enter the seconds of first timestamp: "))

h2 = int(input("Enter the hours of second timestamp: "))
m2 = int(input("Enter the minutes of second timestamp: "))
s2 = int(input("Enter the seconds of second timestamp: "))

t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2
diff = abs(t1-t2)

print("The difference between given timestamps in seconds is", diff)