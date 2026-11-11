'''Digital access control using bitwise operators: Core permissions are represented by bits in
   a number.
   1)bit 0 -> read
   2)bit 1 -> write
   3)bit 2 -> execute
   4)bit 3 -> admin
   Accept a permission number and a permission bit number. Determine whether a permission is
   enable using bitwise operator'''

per_num = int(input("Enter the permmission number: ")) 
print("0 -> Read\n1 -> Write\n2 -> Execute\n3 -> Admin")
per_bit_num = int(input("Enter the permission bit number(0-3): "))
permissions = ("Read", "Write", "Execute", "Admin")
if 0<=per_bit_num<=3:
   output = per_num & (1<<per_bit_num)
   if 1 == (output>>per_bit_num):
      print(permissions[per_bit_num], "is enabled!")
   else:
      print(permissions[per_bit_num], "is disabled!")
else:
   print("Invalid permission bit number!")