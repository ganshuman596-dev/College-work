'''Problem Statement: A college is taking 3 groups of students for an industrial visit.
   Each bus can accomodate 40 students. 
   Given the number of students in the groups, calculate the minmum number of busses required.'''
import math

group1 = int(input("Enter the number of students in group 1: "))
group2 = int(input("Enter the number of students in group 2: "))
group3 = int(input("Enter the number of students in group 3: "))

total_students = group1+group2+group3
busses_required = math.ceil(total_students/40)

print(f'Total {busses_required} busses are required.')