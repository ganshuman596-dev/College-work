'''IOT sensor alert system: A temperature sensor reports a value and a pressure sensor 
   reports an another value. Print-
        1)Critical => temperature>=80 and pressure>=150
        2)Warning => temperature>=60 or pressure>=100
        3)Normal => Otherwise
        4)If both critical and warning conditions are true, critical takes priority'''

temp = int(input("Enter the temperature in degree celsius: "))
pressure = int(input("Enter the pressure: "))

if temp>=80 and pressure>=150:
    print("CRITICAL!")
elif temp>=60 or pressure>=100:
    print("WARNING!")
else:
    print("NORMAL!")