import math

stu1 = int(input("Enter the number of students in first class: "))
stu2 = int(input("Enter the number of students in second class: "))
stu3 = int(input("Enter the number of students in third class: "))

desk1 = math.ceil(stu1/2)
desk2 = math.ceil(stu2/2)
desk3 = math.ceil(stu3/2)
total_desk = desk1+desk2+desk3

print("The minimum required benches are:", total_desk)
