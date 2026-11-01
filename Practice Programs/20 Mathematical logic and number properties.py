'''Mathematical logic and number properties: Find all armstrong numbers in a range L and R. 
   Expect two integers L and R. Print every armstrong number in that range without converting 
   a number to string'''

l = int(input("Enter the start of range: "))
r = int(input("Enter the end of range: "))
for i in range(l+1, r):
    og_num = i
    count = 0
    x = i
    while x>0:
        count+=1
        x = x//10
    y = i
    arm_sum = 0
    while y>0:
        arm_sum = arm_sum + ((y%10)**count)
        y = y//10
    if arm_sum == og_num:
        print(og_num, "is armstrong number")