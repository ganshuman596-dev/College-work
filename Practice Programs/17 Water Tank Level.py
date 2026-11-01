'''Problem Statement: A water tank has capacity of 1000 litre. The current water level is given in percentage.
                      Write a python program to calculate-
                      1)Current water level quantity in litre
                      2)Remaining capacity in litre
                      3)Display whether tank is
                       -empty for 0%
                       -low for below 20%
                       -normal for 20% to 80%
                       -high for above 80%'''

level = float(input("Enter the water level in percent: "))

in_litre = (level/100)*1000

print(f'Current water level quantity: {in_litre} litre')
print(f'Remaining capacity: {1000-in_litre} litre')

if level == 0:
    print("Tank is EMPTY!")
elif 0<level<=20:
    print("Tank has LOW level of water!")
elif 20<level<=80:
    print("The tank has NORMAL level of water.")
else:
    print("The tank has HIGH level of water!")
    