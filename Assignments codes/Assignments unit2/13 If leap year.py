# Program to check if a year is leap year

year = int(input("Enter the year: "))

if year%400==0 or (year%4==0 and year%100!=0):
    print(f'The year {year} is leap year')
else:
    print(f'The year {year} is not leap year')
    