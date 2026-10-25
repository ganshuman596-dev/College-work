#Program to check if a date is valid

d = int(input("Enter the day: "))
m = int(input("Enter the month: "))
y = int(input("Enter the year: "))

valid = False
if y>0:
    if 0<m<=12:
        if m in [4, 6, 9, 11]:
            if 0<d<=30:
                valid = True
        elif m == 2:
            if y%400==0 or (y%4==0 and y%100!=0):
                if 0<d<=29:
                    valid = True
            else:
                if 0<d<=28:
                    valid = True
        else:
            if 0<d<=31:
                valid = True

if valid:
    print(f'{d}/{m}/{y} is valid date')
else:
    print(f'{d}/{m}/{y} is invalid date')
