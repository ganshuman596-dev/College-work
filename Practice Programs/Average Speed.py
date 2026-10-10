'''Prblem Statement: A vehicle travels a certain distance in two stages.
                     Given: dist1, time1
                            dist2, time2
                     Calculate the average speed.'''

dist1 = int(input("Enter the diastance covered in first stage: "))
time1 = int(input("Enter the time required in first stage: "))
dist2 = int(input("Enter the diastance covered in second stage: "))
time2 = int(input("Enter the time required in second stage: "))

avg = (dist1+dist2)/(time1+time2)

print(f'The average speed is = {avg}')