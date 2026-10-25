'''In bowling, the player starts with 10 pins at the far end of a lane. The object is to knock all the pins down.
For this exercise, the number of pins and balls will vary. Given the number of pins N and then the number of balls 
K to be rolled, followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing 
after all the balls have been rolled. The balls are numbered from 1 to N (inclusive) for this situation. 
The subsequent number pairs, one for each K represent the start to stop (inclusive) positions of the pins that 
were knocked down with each role. Print a sequence of N characters, where "I" represents a pin left standing and 
"." represents a pin knocked down.'''

n = int(input("Enter the number of pins: "))
k = int(input("Enter the number of balls: "))
seq = ["I"]*n
for b in range(1,k+1):
    s,e = map(int, input("Enter the start and end of fallen pin's range: ").split(" "))
    for p in range(s-1,e):
        seq[p] = "."
print("".join(seq))