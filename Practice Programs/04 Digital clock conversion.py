'''Problem Statement: A digital clcok shows time as hours, minutes and seconds.
                      Calculate total number of seconds, ellapsed since midnight.'''

h = int(input("Enter the hours: "))
m = int(input("Enter the minutes: "))
s = int(input("Enter the seconds: "))

total_secs = (h*3600)+(m*60)+s

print(f'The total number of seconds = {total_secs}')