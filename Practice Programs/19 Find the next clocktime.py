'''Find the next cloktime: Accept the hours, minutes, seconds. Calculate the time exactly 
   one second later, handling the transition between second, minutes and hours. '''

h = int(input("Enter the hours(0-23): "))
m = int(input("Enter the minutes(0-59): "))
s = int(input("Enter the seconds(0-59): "))
s+=1
if s==60:
    s=0
    m+=1
    if m==60:
        m=0
        h+=1
        if h==24:
            h=0
print(f'One second later: {h}:{m}:{s}')
