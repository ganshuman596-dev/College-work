'''Problem Statement: A temperature sensor gives a reading in celsius.
                      Classify the machine condition as-
                      1)below 0 degree celsius->Freezing
                      2)0-30 degree celsius->Normal
                      3)31-60 degree celsius->Warning
                      4)Above 60 degree celsius->Critical'''

temp = float(input("Enter the temperature in degree celsius: "))

if temp<0:
    print("Freezing!")
elif 0<=temp<=30:
    print("Normal!")
elif 31<=temp<=60:
    print("Warning!")
else:
    print("Critical!")
    