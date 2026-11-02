'''Balling pin simulation with multiple round: There are N pins in a row. Initially all pins are 
   standing. For each of K balls, a start and end positions are given and all pins in that
   inclusive range are knockdown. Print the final pin arrangement and count the number of pins 
   still standing.'''

n = int(input("Enter number of pins: "))
k = int(input("Enter the number of balls: "))
pins = ["I"]*n
for b in range(1,k+1):
    print("BALL",b)
    s = int(input("Enter the start of range: "))
    e = int(input("Enter the end of range: "))
    for i in range(s,e+1):
        pins[i-1]="."
    if "I" not in pins:
        break
print("".join(pins))
print("Number of pins standing =", pins.count("I"))